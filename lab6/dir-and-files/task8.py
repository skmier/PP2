import os


path = r"C:\Users\saken\OneDrive\Рабочий стол\emptyfile"

if not os.access(path, os.F_OK):
    print("Path doesn`t exist")
else:
     print("Path exists")
     os.remove(path)
     print("File has been removed")