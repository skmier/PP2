def generator_div_by3_4(n):
    for i in range(n):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input("Print n: "))
for i in generator_div_by3_4(n):
    print(i, end=" ")