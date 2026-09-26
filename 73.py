#73. Write a python program to Find the sum of natural numbers using recursion.
def recursive_natural_sum(n):
    return 0 if n == 0 else n + recursive_natural_sum(n - 1)
print("Natural sum of first 5 items:", recursive_natural_sum(5))
