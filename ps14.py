# Write a python program to Count Lowercase letters in a string
text = "Hello Python World!"
lower_count = 0
for char in text:
    if char.islower():
        lower_count += 1
print("Lowercase letter count:", lower_count)
