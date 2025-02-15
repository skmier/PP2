import math
n = int(input("Input number of sides: "))
length = int(input("Input the length of a side: "))
s = (n * pow(length,2)) / (4 * math.tan(math.pi / n))
print(f"The area of the polygon is: {s}")