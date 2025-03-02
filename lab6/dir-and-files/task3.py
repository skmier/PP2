import os

path = r"C:\Users\saken\OneDrive\Рабочий стол\PP2"

if not os.access(path, os.F_OK):
    print("Past doesn`t exist")
else:
    print("Path exists ")
    print(f"Name of files : {os.path.basename(path)}")
    print(f"name of dir : {os.path.dirname(path)}")
