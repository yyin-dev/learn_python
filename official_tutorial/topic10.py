def line():
    print("-"*20)

import os
print(os.getcwd())
os.chdir("C:/users/musicman/Desktop/learn_python/official_tutorial")
os.system("ls")
line()

import shutil  # For file and directory management

import glob  # Making file list from directory wildcard searches
print(glob.glob("*.py"))
line()

import sys
print(sys.argv)
line()

import argparse
parser = argparse.ArgumentParser(description="An argparser example")


