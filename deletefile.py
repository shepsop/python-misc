import os

path = "c:\\users\\robert\\copytest2.txt"

try:

    os.remove(path)

except FileNotFoundError:
    print("file not found")