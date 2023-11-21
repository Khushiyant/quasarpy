'''This module contains the main() function, which is the entry point for the
command line interface.'''
from dotenv import load_dotenv

load_dotenv()

__version__ = '0.1.0'

def main():
    import sys
    from quasar.cli import program, logger

    if not sys.argv[1:]:
        sys.argv.append('-h')
    try:
        with open('./assets/quasar.txt', 'r') as art:
            print(art.read())
        program()
    except Exception as e:
        logger.log(e)
        

if __name__ == "__main__":
    main()