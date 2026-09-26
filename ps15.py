# Write a python program to Count digits in a string
text = "Python 3.10 released in 2021"
digit_count = 0
for char in text:
    if char.isdigit():
        digit_count += 1
print("Digit count:", digit_count)
