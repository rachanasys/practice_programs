#78. Write a python program to Calculate sum of digits using recursion.
def recursive_digit_sum(n):
    return n if n < 10 else (n % 10) + recursive_digit_sum(n // 10)
print("Digit sum of 5432:", recursive_digit_sum(5432))
