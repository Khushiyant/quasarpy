import click
from typing import List, Callable, Optional
from quasar.utils.logger import logger
from quasar.utils import JsonFormatter, XmlFormatter
from quasar.utils import formatted_data
from quasar.algorithm import detect_smell, MainDetector
from quasar.handler import IssueHandler, Issue

from quasar import __version__
from quasar.algorithm import train
from quasar.types import ModelType, SmellType, FormatterType
from quasar.utils import ASCII_ART
from quasar.utils import analyse


class ASCIICommandClass(click.Group):
    def get_help(self, ctx):
        return ASCII_ART + '\n' + super().get_help(ctx)


@click.group(name='cli', cls=ASCIICommandClass)
@click.version_option(__version__, prog_name='Quasar')
@click.help_option('-h', '--help')
def cli():
    pass


@cli.command(name='train', help='Train a random forest model')
@click.option('--dataset', '-dt')
@click.option('--output', '-o')
@click.option('--type', '-t',
              type=click.Choice([m.value for m in ModelType]))
def train_model(type, dataset, output):
    train(type, output, dataset)


@cli.command(name='detect', help='Detect code smells')
@click.option('--type', '-tp')
@click.option('--path', '-p')
@click.option('--format', '-f',
              type=click.Choice([t.value for t in FormatterType]))
def detect(type, path, format):
    """
    Detects the specified type of object in the given path and formats the output.

    Args:
        type (str): The type of object to detect.
        path (str): The path to the file or directory to be analyzed.
        format (str): The desired output format ('json' or 'xml').

    Raises:
        click.BadParameter: If the path is not provided.

    Returns:
        None
    """
    detector = MainDetector()
    formatter = JsonFormatter() if format == FormatterType.JSON.value else XmlFormatter()

    if path:
        click.echo(analyse(path, 'raw'))
    else:
        raise click.BadParameter('Path is required')


if __name__ == '__main__':
    cli()
