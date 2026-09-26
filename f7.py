# write a python program to If a number is perfect using function 
def is_perfect_number(n):
    if n <= 1:
        return False
    # Find all proper divisors and sum them up
    divisor_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisor_sum == n
print(is_perfect_number(6))
print(is_perfect_number(5))
