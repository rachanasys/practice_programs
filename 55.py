#55.  Write a python program to Print a pyramid pattern of stars.
rows = 5

# The loop aligns spaces and stars centered row by row to form a upright pyramid structure
for i in range(rows):
    print(" " * (rows - i - 1) + "*" * (2 * i + 1))
