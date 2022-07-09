import os
import sys
import argparse


def is_file(files: str) -> bool:
    """
    Check if given argument 'file' is a real file (files)

    Parameters
    ----------
    files : str
        File names separated by ';'

    Returns
    -------
    bool
        False if any element is not a file, otherwise is True
    """
    for file in files.split(";"):
        if not os.path.isfile(file):
            return False
    return True


def main():
    # handle arguments
    allowed_actions = [
        "MostFrequentIP",
        "LeastFrequentIP",
        "EventsPerSecond",
        "TotalAmountOfBytesExchanged",
    ]
    allowed_types = ["squid"]
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f",
        "--files",
        help="Path to log files, separated by ';' or directory with log files",
        required=True,
    )
    parser.add_argument(
        "-a", "--action", help=f"Actions: {', '.join(allowed_actions)}", required=True
    )
    parser.add_argument(
        "-t", "--type", help="Type of log file, default is 'squid'", default="squid"
    )
    args = parser.parse_args()
    if args.action not in allowed_actions:
        sys.exit(
            f"-a/--action not allowed, allowed actions: {', '.join(allowed_actions)}"
        )
    if args.type not in allowed_types:
        sys.exit(f"-t/--type not allowed, allowed types: {', '.join(allowed_types)}")
    if not (os.path.isdir(args.files) or is_file(args.files)):
        sys.exit(f"-f/--files not allowed, are not valid files or directory")


if __name__ == "__main__":
    main()
