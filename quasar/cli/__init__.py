import click
import os
from datetime import datetime
from quasarpy._version import __version__ as _version
from quasarpy.utils import ASCII_ART
from quasarpy.utils import analyse
from quasarpy.algorithm.detector import MainDetector, detect_smell
from quasarpy.handler.issue import IssueHandler, Repository
from quasarpy.utils.redis_server import generate_report, RedisConfig
import asyncio
from quasarpy.algorithm import LLM, LLMConfig

class ASCIICommandClass(click.Group):
    def get_help(self, ctx):
        return ASCII_ART + "\n" + super().get_help(ctx)


@click.group(name="cli", cls=ASCIICommandClass)
@click.version_option(_version, prog_name="Quasar")
@click.help_option("-h", "--help")
def cli() -> None:
    pass


@cli.command(name="detect", help="Detect code smells")
@click.option(
    "--path",
    "-p",
    type=click.Path(exists=True),
    help="Path to the directory to analyse",
)
@click.option(
    "--format",
    "-f",
    type=click.Choice(["json", "pdf", "html"]),
    help="Format of the report",
)
@click.option(
    "--solution", "-s", is_flag=True, help="Provide solutions for detected code smells"
)
@click.option(
    "--create-issue", "-c", is_flag=True, help="Create an issue if a smell is detected"
)
@click.option(
    "--output", "-o", type=click.Path(exists=False), help="Output file path for report"
)
@click.option(
    "--offline", is_flag=False, help="Use the offline version of the model"
)
def detect(path, format, solution, create_issue, output, offline) -> None:
    """
    Detects the specified type of object in the given path and formats the output.

    Args:
        path (str): The path to the file or directory to be analyzed.
        format (str): The desired output format ('json' or 'xml').
        solution (bool): Whether to provide solutions for the detected code smells.
        create_issue (bool): Whether to create an issue for the detected code smells.
        output (str): The path to save the output report.

    Raises:
        ValueError: If the path is not provided or if format and output path are required but not provided.
        NotImplementedError: If the solution flag is set to True (not implemented yet) or if other formats are not implemented yet.

    Returns:
        None
    """
    issue_handler = IssueHandler(repo=Repository()) if create_issue else None
    redis_config = RedisConfig()

    if solution:
        raise NotImplementedError("Solution flag not implemented yet")
    else:
        try:
            if path:
                data_json = analyse([path])
                if format in ["json", "pdf", "html"]:
                    try:
                        llm_config = LLMConfig()
                        llm = LLM(llm_config, is_online=True if not offline else False)

                        detector = MainDetector(llm=llm, issue_handler=issue_handler)
                        data = asyncio.run(detect_smell(data_json, detector))

                        if not format or not output:
                            raise ValueError("Format and output path are required")

                        report_path = os.path.join(
                            output,
                            f'report_{datetime.now().strftime("%H%M%S")}',
                        )

                        if format == "json":
                            with open(report_path, "w") as f:
                                f.write(data)
                        else:
                            if not data:
                                raise ValueError("No data to write")

                            generate_report(
                                config=redis_config,
                                format=format,
                                data=data,
                                report_path=report_path,
                            )

                    except Exception as e:
                        raise e
                else:
                    raise NotImplementedError("Other format not implemented yet")
            else:
                raise ValueError("Path is required")
        except Exception as e:
            raise e


if __name__ == "__main__":
    cli()
