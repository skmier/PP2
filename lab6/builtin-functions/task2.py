def calculate(word):
    upp = 0 
    low = 0
    for i in word:
        if i.isupper():
            upp += 1
        if i.islower():
            low += 1
    print(f"Uppercase letters: {upp} , Lowercase letters: {low}")

word = input()
calculate(word)
