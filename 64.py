#64. Write a python program to Define a function that finds the maximum of three numbers.
def find_max(a, b, c):
    return a if (a >= b and a >= c) else (b if b >= c else c)

print("Max of 10, 20, 15:", find_max(10, 20, 15))

