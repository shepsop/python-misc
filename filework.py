import os

path = "c:\\temp\\pyfolder"

if os.path.exists(path):
    print("This path exists")
    if os.path.isfile(path):
        print("This is a file")
    elif os.path.isdir(path):
        print("This is a folder")
else:
    print("This path does not exist")