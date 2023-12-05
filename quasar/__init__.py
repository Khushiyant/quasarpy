'''This module contains the main() function, which is the entry point for the
command line interface.'''
from dotenv import load_dotenv
from logging import ERROR, INFO, DEBUG
from quasar.utils import ASCII_ART

load_dotenv()

__version__ = '0.1.0'


def main():
    import sys
    from quasar.cli import logger, cli

    try:
        print(ASCII_ART)
        cli()
    except Exception as e:
        logger.log(level=INFO, msg=e)


if __name__ == "__main__":
    main()
