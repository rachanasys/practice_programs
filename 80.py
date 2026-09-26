#80. Write a python program to Print numbers from ‘n’ to 1 using recursion.
def print_countdown(n):
    if n > 0:
        print(n, end=" ")
        print_countdown(n - 1)
print("Countdown sequence:")
print_countdown(5)
print()
