file = open("lab6/something.txt", "a")
something = list(map(str, input().split()))

for i in something:
    file.write(i + "\n")

file.close
file = open("lab6/something.txt", "r")
file.read()
file.close()