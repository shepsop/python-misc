import os

source = "c:\\temp\\copytest.txt"
dest = "c:\\users\\robert\\copytest2.txt"

try:

    if os.path.exists(dest):
        print("file already exists")
    else:
        os.replace(source,dest)
        print(source + " was moved")

except FileNotFoundError:
    print("source file not found")
