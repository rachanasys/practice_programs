#71. Write a python program to Calculate factorial using recursion.
def direct_fact(n):
    return 1 if n == 0 else n * direct_fact(n - 1)
print("Factorial value of 6:", direct_fact(6))
