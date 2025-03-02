import os 
def check(path):
    if os.access(path, os.F_OK):
        print("Path exists")
    else:
        print("Path doesn`t exist")
    if os.access(path, os.R_OK):
        print("Path is readble")
    else:
        print("Path isn`t readble")
    if  os.access(path, os.W_OK):    
        print("Path is writable")
    else:
        print("'Path isn`t writable")
    if  os.access(path, os.X_OK): 
        print("Path is executable:") 

    else:
        print("Path isnt executable:")

path = r"C:\Users\saken\OneDrive\Рабочий стол\PP2"
check(path)

