'''This module contains the main() function, which is the entry point for the
command line interface.'''
from dotenv import load_dotenv
from logging import INFO
from quasar.cli import cli
from quasar.utils import logger
from quasar._version import __version__ as _version
__version__ = _version

load_dotenv()  # Load environment variables from .env file


def main():

    try:
        cli()
    except Exception as e:
        logger.log(level=INFO, msg=e)


if __name__ == "__main__":
    main()
