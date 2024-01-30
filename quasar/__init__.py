'''This module contains the main() function, which is the entry point for the
command line interface.'''
from dotenv import load_dotenv
from logging import ERROR, INFO, DEBUG


load_dotenv() # Load environment variables from .env file

__version__ = '0.1.0'


def main():
    from quasar.cli import logger, cli

    try:
        cli()
    except Exception as e:
        logger.log(level=INFO, msg=e)


if __name__ == "__main__":
    main()
