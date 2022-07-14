from ast import arg
import os
import sys
import argparse

from sources import squid

# some constants
# types of logs
SQUID = "squid"
# actions
MOST_FREQUENT_IP = "MostFrequentIP"
LEAST_FREQUENT_IP = "LeastFrequentIP"
EVENTS_PER_SECOND = "EventsPerSecond"
TOTAL_AMOUNT_OF_BYTES_EXCHANGED = "TotalAmountOfBytesExchanged"


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
        MOST_FREQUENT_IP,
        LEAST_FREQUENT_IP,
        EVENTS_PER_SECOND,
        TOTAL_AMOUNT_OF_BYTES_EXCHANGED,
    ]
    allowed_types = [SQUID]
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
        "-t", "--type", help=f"Type of log file, default is '{SQUID}'", default=SQUID
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

    # do the magic
    if args.type == SQUID:
        if os.path.isdir(args.files):
            files = [f"{args.files}/{file}" for file in os.listdir(args.files)]
        else:
            files = args.files.split(";")
        factory = squid.Squid(files)

    if args.action == MOST_FREQUENT_IP:
        result = factory.most_frequent_IP()
        print(result.json())

    if args.action == LEAST_FREQUENT_IP:
        result = factory.least_frequent_IP()
        print(result.json())

    if args.action == EVENTS_PER_SECOND:
        result = factory.events_per_second()
        print(result.json())

    if args.action == TOTAL_AMOUNT_OF_BYTES_EXCHANGED:
        result = factory.total_amount_of_bytes_exchanged()
        print(result.json())


if __name__ == "__main__":
    main()
