import argparse
import logging
from pathlib import Path

from polyrename.driver import driver_dev, driver_gui


def _parse_args():
    parser = argparse.ArgumentParser(
        description="A cross-platform, bulk-file rename tool"
    )
    parser.add_argument("--verbose", "-v", action="count", default=0, help="Verbosity")
    parser.add_argument("-mode", choices=["gui", "dev"], default="gui", help="UI Mode")
    parser.add_argument("-files", nargs="+", default=[], help="Files to Rename")

    return parser.parse_args()


def main():
    args = _parse_args()

    if args.verbose == 0:
        logging.basicConfig(level=logging.WARNING)
    elif args.verbose == 1:
        logging.basicConfig(level=logging.INFO)
    elif args.verbose >= 2:
        logging.basicConfig(level=logging.DEBUG)

    mode = args.mode
    files = [
        Path(file)
        for file in args.files
        if Path(file).exists() and Path(file).is_file()
    ]

    if mode == "gui":
        driver_gui.main(files)
    elif mode == "dev":
        driver_dev.main(files)


if __name__ == "__main__":
    main()
