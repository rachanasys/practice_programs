#76. Write a python program to Find GCD of 2 numbers using recursion.
def recursive_gcd(a, b):
    return a if b == 0 else recursive_gcd(b, a % b)
print("GCD of 48 and 18:", recursive_gcd(48, 18))
