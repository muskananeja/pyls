 
#goal is to implement a python command line tool called py;
#mimics unix ls command
#using fun
import os
# os allows and provides functions to interact with the operating system 
#os.listdir() returns a list containing the names of the entries in the directory given by the path

import argparse
import time


def parse_arguments():
    parser = argparse.ArgumentParser(description="Python implementation of Unix 'ls' command")
    parser.add_argument('-l', '--long', action='store_true', help='use a long listing format')
    return parser.parse_args()


def listout():
    args = parse_arguments()
    entries = os.listdir(".")
    for entry in entries:
        print(entry)

def listout():
    args = parse_arguments()
    entries = os.listdir(".")
    for entry in entries:
        if args.long:
            file_stat = os.stat(entry)
            permissions = oct(file_stat.st_mode)[-3:]
            file_size = file_stat.st_size
            modification_time = time.strftime('%Y-%m-%d %H:%M', time.localtime(file_stat.st_mtime))
            print(f"{permissions} {file_size} {modification_time} {entry}")
        else:
            print(entry)


if __name__ == "__main__":
    listout()

def listout():
    entries = os.listdir(".")
    for entry in entries:
        print(entry)
