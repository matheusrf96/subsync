#coding: utf-8

from content.io import *
from content.timeConverter import *

filepath = raw_input("Insert the name of the a file to be updated: ")
time = input("Insert how many seconds you want to delay(negative number[use '-' before the number]) or haste(positive number[without '+']) the subtitles: ")

if writeNewFile(getNewFile(filepath, time), filepath):
    print("A new file was created!")
else:
    print("Error!")
