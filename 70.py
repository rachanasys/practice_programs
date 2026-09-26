#70. Write a python program to Define a function that calculates power of a number using recursion.
def recursive_power(base, exp):
    return 1 if exp == 0 else base * recursive_power(base, exp - 1)
print("2 raised to power 4:", recursive_power(2, 4))
