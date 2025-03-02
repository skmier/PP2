my_list = list(map(int, input().split()))

x = '*'.join(str(i) for i in my_list)
print(eval(x))