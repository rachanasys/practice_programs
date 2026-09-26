# write a python program to Check if a number is armstrong using function 
def is_armstrong(n):
    s = str(n)
    power = len(s)
    total = sum(int(digit) ** power for digit in s)
    return total == n
print(is_armstrong(153))
print(is_armstrong(53))
