from string import ascii_uppercase
import os
for i in ascii_uppercase:
    file_name = i+".txt"
    with open(file_name, "w") as file:
        file.write(f"{i} file")
