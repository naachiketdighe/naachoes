import os
from os import path
import datetime
from datetime import date, time , timedelta
import time
import shutil
print(os.name)
# opening a file
b = open("textfile.txt", "w")
# printing the first 10 numbers in the text file
for i in range (0,10) :
    b.write("Number " + str(i) + "\n")
b.close()
# modifying a file in python/ appending text onto a file
k = open("textfile.txt", "a")
for i in range (0,10) :
    k.write("Number " + str(i+10) + "\n")
k.close()

# to check if an item exists
print("item exists: " + str(path.exists("textfile.txt")))
# check if item is a file
print("Item file: " + str(path.isfile("textfile.txt")))
# check if item is a directory
print("Item is a directory: " + str(path.isdir("textfile.txt")))

# working with file paths
print("File path is: " + str(path.realpath("textfile.txt")))
# splitting file path and name
print("File name and path are " + str(path.split(path.realpath("textfile.txt"))))

# get the time the file was modified
print("last modified: " + time.ctime(path.getmtime("textfile.txt")))

# calculate how long ago the file was midifed
bd = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
print("The file was modified: " + str(bd.total_seconds()) + " seconds")

# to make a dupliacte of a file
if path.exists("textfile.txt"):
    pth = path.realpath("textfile.txt")
    # to make a backup file
    backup = pth + ".bak"
    # use shutil to copy
    shutil.copy(pth,backup)
    shutil.copystat(pth,backup)

# to rename the original file
# os.rename("textfile.txt", "tuxtfile.txt")

# supressing a file into a ZIP
front , tail = path.split(path.realpath("textfile.txt"))
shutil.make_archive("archeive_file", "zip" , front)
