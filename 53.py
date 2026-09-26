#53. Write a python program to Print all Odd numbers between 1 and 100.

# The range function starts at 1 and steps by 2 to generate only odd numbers up to 100
for num in range(1, 101, 2):
    print(num, end=" ")
print()
