'''This module contains the main() function, which is the entry point for the
command line interface.'''
from dotenv import load_dotenv
from quasarx.cli import cli
from quasarx.utils import logger
from quasarx._version import __version__ as _version

__version__ = _version

load_dotenv()  # Load environment variables from .env file


def main():
    '''Entry point for the command line interface.'''
    logger.info(f"Quasar {_version} started")
    try: 
        cli()
    except NotImplementedError as e:
        logger.error(e)
    except ValueError as e:
        logger.error(e)
    finally:
        logger.info(f"Quasar {__version__} stopped")
    

if __name__ == "__main__":
    main()
