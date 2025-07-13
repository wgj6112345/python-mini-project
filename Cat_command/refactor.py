
class CatError(Exception):
    pass

class Logger:
    def __init__(self,verbosity=False):
        self.verbose = verbosity

    def error(self, msg):
        print(f'ERROR: {msg}')


logger = Logger()

# logger.error("我是错误")

import argparse
from pathlib import Path
import os

def read_file(filename) -> None:

    if filename.is_dir():
        logger.error(f'filepath {filename} is dir')
        return 
    
    try:
        with open(filename) as f:
            for line in f:
                print(line, end = '')
    except Exception as e:
        logger.error(f"ERROR reading file {e}")

def cli() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="cat",
        description="cat command implemention",
        epilog="Example: yourpath/file.txt"
    )

    parser.add_argument(
        "source",
        type=Path,
        help="source file"
    )

    return parser.parse_args()

def main() -> None:
    args = cli()

    try:
        read_file(args.source)
    except CatError as e:
        logger.error(f"{e}")
        exit(code=1)
    except KeyboardInterrupt:
        logger.error(f"\nInterrupt")

if __name__ == "__main__":
    main()