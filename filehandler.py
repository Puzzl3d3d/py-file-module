class openFile:
    def __init__(self, file_name):
        #self.file = open(file_name, "w")
        self.filename = file_name
    def writeLine(self, contents):
        file = open(self.filename,"w")
        file.write(f"\n{contents}")
        file.close()
    def write(self, contents):
        file = open(self.filename,"w")
        file.write(f"{contents}")
        file.close()
    def append(self, contents):
        file = open(self.filename,"a")
        file.write(f"{contents}")
        file.close()
    def appendLine(self, contents):
        file = open(self.filename,"a")
        file.write(f"\n{contents}")
        file.close()
    def readLineRange(self, linemin, linemax):
        file = open(self.filename, "r")
        lines = file.readlines()
        file.close()
        desired_lines = lines[linemin:linemax]
        return desired_lines
    def readLine(self, line):
        file = open(self.filename, "r")
        lines = file.readlines()
        file.close()
        desired_line = lines[line:line]
        return desired_line
    def read(self):
        file = open(self.filename, "r")
        contents = file.read()
        file.close()
        return contents
    def printRead(self):
        file = open(self.filename, "r")
        contents = file.read()
        file.close()
        print(contents)
        return contents
    def empty(self):
        file = open(self.filename, "w")
        file.write("")
        file.close()
    def emptyWithLine(self, content):
        file = open(self.filename, "w")
        file.write(f"{content}")
        file.close()
    def emptyWithContent(self, content):
        file = open(self.filename, "w")
        file.write(f"{content}")
        file.close()
    def writeLines(self, *lines):
        lines = "\n".join(lines)
        self.write(lines)
    def close(self):
        pass
    def fileno(self):
        file = open(self.filename, "r")
        fileno = file.fileno()
        file.close()
        return detach
    def isatty(self):
        file = open(self.filename, "r")
        isatty = file.isatty()
        file.close()
        return isatty
    def tell(self):
        file = open(self.filename, "r")
        tell = file.tell()
        file.close()
        return tell
    def truncate(self, num):
        file = open(self.filename, "a")
        file.truncate(num)
        file.close()
    def filename(self):
        return self.filename
def openFileFunc(file_name):
    return openFile(file_name)

file =  openFile("filename.txt")

file.write("I have written to the file!")
file.appendLine("I have added another line!")
file.truncate(0)
file.write("Now my data is gone!")
file.append("\nNow my file has even more data!")
file.appendLine("And more!")