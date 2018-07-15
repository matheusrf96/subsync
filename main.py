#coding: utf-8

from content.io import *
from content.timeConverter import *

filepath = raw_input("Insert the name of the a file to be updated: ")
time = input("Change (seconds): [Ex.: +20 | -5] ")

if writeNewFile(getNewFile(filepath, time), filepath):
    print("A new file was created!")
else:
    print("Error!")