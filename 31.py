#31. Write a python program To Check if a number is an Armstrong number.
n = 153
print(n == sum(int(d)**len(str(n)) for d in str(n)))












