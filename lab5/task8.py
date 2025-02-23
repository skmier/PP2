import re

with open("lab5/row2.txt") as file:
    data = file.read()
print(re.findall(r"[A-Z][^A-Z]*", data))