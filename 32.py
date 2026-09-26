#32. Write a python program To Check if a number is a perfect number.
n = 28
print(n == sum(i for i in range(1, n) if n % i == 0))



