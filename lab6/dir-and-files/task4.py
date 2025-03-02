import os 

with open("lab5/row.txt", "r") as file:
    data = file.read()
print(len(list(data.split("\n"))))