from os import write


test = "line 1\nline 2\nline3"

with open("c:\\users\\robert\\test.txt","w") as file:
    file.write(test)