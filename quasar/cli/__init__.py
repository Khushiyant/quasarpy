import click
from typing import List, Callable, Optional
from quasar.utils.logger import logger
from quasar.utils import JsonFormatter, XmlFormatter
from quasar.utils import formatted_data
from quasar.algorithm import detect_smell, ClassDetector, MethodDetector
import os
from quasar.handler import IssueHandler, Issue
from enum import Enum
import radon
from quasar import __version__
from quasar.algorithm import train
from quasar.config import ModelType, SmellType, FormatterType


@click.group(name='cli')
@click.option('--debug/--no-debug', default=False)
@click.pass_context
def cli(ctx, debug):
    ctx.ensure_object(dict)

    ctx.obj['DEBUG'] = debug


@cli.command(name='train', help='Train a random forest model')
@click.option('--dataset', '-dt')
@click.option('--output', '-o')
@click.option('--type', '-t',
              type=click.Choice([ModelType.CLASS.value, ModelType.METHOD.value]))
def train_model(dataset, output):
    train(type, dataset, output)


@cli.command(name='version', help='Show the version of Quasar')
def version():
    click.echo(f"Quasar version {__version__}")


@cli.command(help='Sync the context mode')
@click.pass_context
def sync(ctx):
    click.echo(f"Debug is {'on' if ctx.obj['DEBUG'] else 'off'}")


def main():
    cli()


if __name__ == '__main__':
    main()
