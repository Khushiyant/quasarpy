import click
from typing import List, Callable, Optional
from quasar.utils.logger import logger
from quasar.utils import JsonFormatter, XmlFormatter
from quasar.utils import formatted_data
from quasar.algorithm import detect_smell, ClassDetector, MethodDetector
import os
from quasar.handler import IssueHandler, Issue
from radon import complexity
from quasar import __version__
from quasar.algorithm import train
from quasar.config import ModelType, SmellType, FormatterType
from quasar.utils import ASCII_ART


class CustomCommandClass(click.Group):
    def get_help(self, ctx):
        return ASCII_ART + '\n' + super().get_help(ctx)


@click.group(name='cli', cls=CustomCommandClass)
@click.version_option(__version__, prog_name='Quasar')
@click.help_option('-h', '--help')
def cli():
    pass


@cli.command(name='train', help='Train a random forest model')
@click.option('--dataset', '-dt')
@click.option('--output', '-o')
@click.option('--type', '-t',
              type=click.Choice([ModelType.CLASS.value, ModelType.METHOD.value]))
def train_model(type, dataset, output):
    train(type, dataset, output)


@cli.command(name='detect', help='Detect code smells')
@click.option('--type', '-tp')
@click.option('--path', '-p', default=os.getcwd())
@click.option('--format', '-f',
              type=click.Choice([FormatterType.JSON.value, FormatterType.XML.value]))
def detect(type, path, format):
    detector = ClassDetector() if type == ModelType.CLASS.value else MethodDetector()
    formatter = JsonFormatter() if format == FormatterType.JSON.value else XmlFormatter()

    if os.path.exists(path):
        if os.path.isdir(path):
            for root, dirs, files in os.walk(path):
                for file in files:
                    if file.endswith('.py'):
                        file_path = os.path.join(root, file)
                        data = complexity.cc_visit(file_path)
                        # smell = detect_smell(data, detector)
                        # formatted_data = formatter.format(file_path, smell)
                        # click.echo(formatted_data)
                        click.echo(data)
        elif os.path.isfile(path):
            data = complexity.cc_visit(path)
            # smell = detect_smell(data, detector)
            # formatted_data = formatter.format(path, smell)
            # click.echo(formatted_data)
            click.echo(data)


if __name__ == '__main__':
    cli()
