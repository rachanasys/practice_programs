# Write a python program to Count upper case letters in a string 
text = "Hello Python World!"
upper_count = 0
for char in text:
    if char.isupper():
        upper_count += 1
print("Uppercase letter count:", upper_count)
