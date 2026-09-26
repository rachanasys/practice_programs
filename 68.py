#68. Write a python program to Define a function that returns the sum of digits of a number.
def sum_digits_func(n):
    return sum(int(digit) for digit in str(abs(n)))
print("Digit sum of 1234:", sum_digits_func(1234))

