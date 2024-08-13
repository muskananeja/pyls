 
#goal is to implement a python command line tool called py;
#mimics unix ls command
#using fun
import os
# os allows and provides functions to interact with the operating system 
#os.listdir() returns a list containing the names of the entries in the directory given by the path

import argparse
import time


def listout():
    entries = os.listdir(".")
#lists all files in current directory "." refers to current directory, stored in entries list
