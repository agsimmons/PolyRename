import argparse
from pathlib import Path

import sys
print(sys.path)

from polyrename.driver import driver_gui, driver_test


def _parse_args():
    parser = argparse.ArgumentParser(
        description="A cross-platform, bulk-file rename tool"
    )
    parser.add_argument("-mode", choices=["gui", "test"], default="gui", help="UI Mode")
    parser.add_argument("-files", nargs="+", default=[], help="Files to Rename")

    return parser.parse_args()


def main(mode, files):
    if mode == "gui":
        driver_gui.main(files)
    elif mode == "test":
        driver_test.main(files)


if __name__ == "__main__":
    args = _parse_args()

    arg_mode = args.mode
    arg_files = [
        Path(file)
        for file in args.files
        if Path(file).exists() and Path(file).is_file()
    ]

    main(arg_mode, arg_files)
