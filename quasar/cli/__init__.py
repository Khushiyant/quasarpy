import click
import os
from datetime import datetime
from quasar._version import __version__ as _version
from quasar.utils import ASCII_ART
from quasar.utils import analyse
from quasar.algorithm.detector import MainDetector, detect_smell
from quasar.handler.issue import IssueHandler, Repository
from quasar.utils.redis_server import generate_report, RedisConfig


class ASCIICommandClass(click.Group):
    def get_help(self, ctx):
        return ASCII_ART + '\n' + super().get_help(ctx)


@click.group(name='cli', cls=ASCIICommandClass)
@click.version_option(_version, prog_name='Quasar')
@click.help_option('-h', '--help')
def cli() -> None:
    pass


@cli.command(name='report', help='Generate a report')
@click.option('--format', '-f',
              type=click.Choice(['json', 'txt']))
@click.option('--output', '-o', type=click.Path(exists=False), help='Output file path')
def report(format, output) -> None:
    """
    Generates a report of the detected code smells.

    Args:
        regenerate (bool): Whether to regenerate the report.

    Returns:
        None
    """
    config = RedisConfig()

    if not format:
        raise ValueError('Format is required')
    report_name = f'report_{datetime.now().strftime("%H%M%S")}.{format}'
    report_path = click.format_filename(os.path.join(output, report_name))
    with open(report_path, 'w') as f:
        data = generate_report(config=config, format=format)
        if not data:
            raise ValueError('No data to write')
        f.write(data)


@cli.command(name='detect', help='Detect code smells')
@click.option('--path', '-p')
@click.option('--create-issue', '-c', is_flag=True, help='Create an issue if a smell is detected')
@click.option('--format', '-f',
              type=click.Choice(['json']))
@click.option('--solution', '-s', is_flag=True, help='Provide solutions for detected code smells')
def detect(path, format, solution, create_issue) -> None:
    """
    Detects the specified type of object in the given path and formats the output.

    Args:
        type (str): The type of object to detect.
        path (str): The path to the file or directory to be analyzed.
        format (str): The desired output format ('json' or 'xml').
        solution (bool): Whether to provide solutions for the detected code smells.

    Raises:
        ValueError('Path is required'): If the path is not provided.

    Returns:
        None
    """
    issue_handler = IssueHandler(repo=Repository()) if create_issue else None

    if solution:
        raise NotImplementedError('Solution flag not implemented yet')
    else:
        try:
            if path:
                data_json = analyse([path])
                if format == 'json':
                    try:
                        detector = MainDetector(issue_handler=issue_handler)
                        click.echo(detect_smell(data_json, detector))
                    except Exception as e:
                        raise e
                else:
                    NotImplementedError('Other format not implemented yet')
            else:
                raise ValueError('Path is required')
        except Exception as e:
            raise e


if __name__ == '__main__':
    cli()
