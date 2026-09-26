#56. Write a python program to Print an inverted pyramid of stars.
rows = 5

for i in range(rows, 0, -1):
    print(" " * (rows - i) + "*" * (2 * i - 1))
