# Write a function that will multiply two positive integers
# without using the '*' operator or bitwise operators 

def recursiveMultiply(x, y):
    if x == 0 or y == 0: return 0
    else: return x + recursiveMultiply(x, y - 1)

print(str(recursiveMultiply(5, 5)))