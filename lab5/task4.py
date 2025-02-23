import re 

with open("lab5/row.txt", encoding="utf-8") as file:
    data = file.read()
m = re.findall(r"[A-Z][a-z]+", data)

print(m)