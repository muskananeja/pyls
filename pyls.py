import os
import argparse
import time

def parse_arguments():
    """
    Parses command-line arguments using argparse.

    Returns:
        argparse.Namespace: An object containing the parsed arguments.
    """
    parser = argparse.ArgumentParser(description="Python implementation of Unix 'ls' command")
    parser.add_argument('-l', '--long', action='store_true', help='use a long listing format')
    parser.add_argument('-F', '--classify', action='store_true', help='classify files with a symbol')
    return parser.parse_args()

def format_entry(entry, args):
    """
    Formats a single entry based on the command-line arguments.

    Args:
        entry (str): The file or directory name.
        args (argparse.Namespace): The parsed command-line arguments.

    Returns:
        str: The formatted entry string.
    """
    assert isinstance(entry, str), "Entry should be a string"
    assert isinstance(args, argparse.Namespace), "Args should be of type argparse.Namespace"
    
    if args.classify:
        if os.path.isdir(entry):
            entry += "/"
        elif os.access(entry, os.X_OK):
            entry += "*"
        return entry
    elif args.long:
        return format_long_entry(entry)
    else:
        return entry

def format_long_entry(entry):
    """
    Formats a single entry in long format.

    Args:
        entry (str): The file or directory name.

    Returns:
        str: The formatted entry string with permissions, size, and modification time.
    """
    file_stat = os.stat(entry)
    permissions = oct(file_stat.st_mode)[-3:]
    file_size = file_stat.st_size
    modification_time = time.strftime('%Y-%m-%d %H:%M', time.localtime(file_stat.st_mtime))
    return f"{permissions} {file_size} {modification_time} {entry}"

def listout():
    args = parse_arguments()
    assert isinstance(args, argparse.Namespace), "Expected args to be an instance of argparse.Namespace"
    entries = os.listdir(".")

    for entry in entries:
        print(format_entry(entry, args))

if __name__ == "__main__":
    listout()
