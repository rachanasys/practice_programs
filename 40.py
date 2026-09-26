#40. Write a python program to Calculate the power of a number without using'**'.
base, exp = 2, 3
res = 1
for _ in range(exp): res *= base
print(res)

