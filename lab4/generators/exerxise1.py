def square_generator(n):
    for i in range(n):
        yield i ** 2

n = int(input())
for i in square_generator(n):
    print(i)