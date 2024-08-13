 
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
    return parser.parse_args()

def listout():
    args = parse_arguments()
    entries = os.listdir(".")
    for entry in entries:
        print(entry)

if __name__ == "__main__":
    listout()

def listout():
    entries = os.listdir(".")
    for entry in entries:
        print(entry)
