#52. Write a python program to Print all even numbers between 1 and 100.

# The range function starts at 2 and steps by 2 to generate only even numbers up to 100
for num in range(2, 101, 2):
    print(num, end=" ")
print()
