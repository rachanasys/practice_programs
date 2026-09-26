#9. Write a python program to check if a number is prime.
n=29
print(n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1)))


