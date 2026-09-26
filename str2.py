#write a python program to Check if a number is prime using recursion
def is_prime(n, divisor=2):
    if n <= 1:
        return False
    if divisor * divisor > n:
        return True
    if n % divisor == 0:
        return False
    return is_prime(n, divisor + 1)
print(is_prime(5))
print(is_prime(10))
