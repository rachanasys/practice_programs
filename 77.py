#77. Write a python program to Find LCM of 2 numbers using recursion.
def find_lcm_via_gcd(a, b):
    def gcd(x, y): return x if y == 0 else gcd(y, x % y)
    return (a * b) // gcd(a, b)
print("LCM of 12 and 15:", find_lcm_via_gcd(12, 15))
