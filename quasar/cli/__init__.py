import click
# from quasar.algorithm import MainDetector

from quasar._version import __version__ as _version
from quasar.utils import ASCII_ART
from quasar.utils import analyse

from radon.cli import log_result


class ASCIICommandClass(click.Group):
    def get_help(self, ctx):
        return ASCII_ART + '\n' + super().get_help(ctx)


@click.group(name='cli', cls=ASCIICommandClass)
@click.version_option(_version, prog_name='Quasar')
@click.help_option('-h', '--help')
def cli() -> None:
    pass


@cli.command(name='detect', help='Detect code smells')
@click.option('--path', '-p')
@click.option('--format', '-f',
              type=click.Choice(['json', 'xml']))
def detect(path, format) -> None:
    """
    Detects the specified type of object in the given path and formats the output.

    Args:
        type (str): The type of object to detect.
        path (str): The path to the file or directory to be analyzed.
        format (str): The desired output format ('json' or 'xml').

    Raises:
        ValueError('Path is required'): If the path is not provided.

    Returns:
        None
    """

    try:
        harvester, cc_harvester, mi_harvester = analyse([path])
        if path:
            click.echo(log_result(harvester, json=( format == 'json' ), xml=( format == 'xml')))
        else:
            raise ValueError('Path is required')
    except Exception as e:
        raise e


if __name__ == '__main__':
    cli()
