import click
from typing import List, Callable, Optional
from quasar.utils.logger import logger
from quasar.utils import JsonFormatter, XmlFormatter
from quasar.utils import formatted_data
from quasar.algorithm import detect_smell, ClassDetector, MethodDetector
import os
from enum import Enum

class SmellType(Enum):
    CLASS = 'CLASS'
    METHOD = 'METHOD'

class FormatterType(Enum):
    JSON = 'JSON'
    XML = 'XML'

@click.command()
@click.argument('--file', , help='The file to analyze.', default='.')
@click.argument('smell_type', required=False, default=SmellType.CLASS.value, choices=click.Choice([s.value for s in SmellType]))
@click.option('--threshold', '-t', default=70, help='The threshold for long methods.')
@click.option('--output', '-o', help='The output format.', default='json', choices=click.Choice([f.value for f in FormatterType]))
def smell(file, thresold, output, smell_type):
    formatter = JsonFormatter() if output == 'json' else XmlFormatter()
    detector = ClassDetector() if smell_type == 'class' else MethodDetector()

    



if __name__ == '__main__':
    smell()
