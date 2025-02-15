def even_generator(n):
    emptlist = []
    for i in range(n):
        if i % 2 == 0:
            yield i
n = int(input("Print n: "))
for i in even_generator(n):
    print(i, end=", ")
