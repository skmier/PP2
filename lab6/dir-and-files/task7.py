with open('lab6/dir-and-files/demo.txt', 'r') as file1, open('lab6/dir-and-files/demo2.txt', 'a') as file2:
    for i in file1:
        file2.write(i)
