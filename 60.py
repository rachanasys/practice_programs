#60. Write a python program to Numbers divisible by 3 &5 up to 100.
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print(num, end=" ")
print()
