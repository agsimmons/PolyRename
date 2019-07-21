import argparse
from pathlib import Path

from polyrename.driver import driver_gui, driver_dev


def _parse_args():
    parser = argparse.ArgumentParser(
        description="A cross-platform, bulk-file rename tool"
    )
    parser.add_argument("-mode", choices=["gui", "dev"], default="gui", help="UI Mode")
    parser.add_argument("-files", nargs="+", default=[], help="Files to Rename")

    return parser.parse_args()


def main():
    args = _parse_args()

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
