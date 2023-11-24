import click
from typing import List, Callable, Optional
from quasar.utils.logger import logger
from quasar.utils import JsonFormatter, XmlFormatter
from quasar.utils import formatted_data
from quasar.algorithm import detect_smell, ClassDetector, MethodDetector
import os
from quasar.handler import IssueHandler, Issue
from enum import Enum


class SmellType(Enum):
    CLASS = 'CLASS'
    METHOD = 'METHOD'


class FormatterType(Enum):
    JSON = 'JSON'
    XML = 'XML'


@click.command()
@click.argument('path', required=True, type=click.Path(exists=True, file_okay=False, dir_okay=True, readable=True))
@click.option('--recursive', '-r', help='Recursively analyze the path.', is_flag=False)
@click.argument('smell_type', required=False, default=SmellType.CLASS.value)
@click.option('--output', '-o', help='The output format.', default='json')#, choices=click.Choice([f.value for f in FormatterType]))
def smell(path, output, smell_type, recursive):
    formatter = JsonFormatter() if output == 'json' else XmlFormatter()
    detector = ClassDetector() if smell_type == 'class' else MethodDetector()
    if smell_type not in [s.value for s in SmellType]:
        raise click.BadParameter(
            'Invalid smell_type. Choices are CLASS or METHOD.')
    if not path:
        raise click.BadParameter('Path is required.')
    if not os.path.exists(path):
        raise click.BadParameter("Invalid value for 'PATH'.")
    if not os.path.isdir(path):
        raise click.BadParameter('Path is not a directory.')


if __name__ == '__main__':
    smell()
