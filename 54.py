#54. Write a python program to Calculate the sum of first ‘n’ natural numbers using a loop.
n = 10
total_sum = 0
# The loop adds every integer from 1 up to n to the running total variable
for i in range(1, n + 1):
    total_sum += i
print(f"Sum of first {n} natural numbers:", total_sum)
