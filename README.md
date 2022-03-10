# py-file-module
A class module for file handling!
# Syntax:
```py
from pyfilemodule import *

file =  openFile("filename.txt") # returns a class of functions

file.write("I have written to the file!")
file.appendLine("I have added another line!")
file.truncate(0)
file.write("Now my data is gone!")
file.append("\nNow my file has even more data!")
file.appendLine("And more!")
file.printRead()
```
