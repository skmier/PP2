def solve(numheads, numlegs):
    rabb = (numlegs - 2 * numheads) // 2
    chick = numheads - rabb
    return f"chikens {chick}, rabbits {rabb}"

heads = int(input("Number of heads: "))
legs = int(input("Number of legs: "))
print(solve(heads, legs))
