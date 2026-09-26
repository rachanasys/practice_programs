#63. Write a python program to Define a function that calculates factorial using recursion.
def recursive_fact(n):
    return 1 if n == 0 else n * recursive_fact(n - 1)
print("Factorial of 5:", recursive_fact(5))

