# Write a python program to Count special characters in a string
text = "User_name@domain.com #1!"
special_count = 0
for char in text:
    if not char.isalnum() and not char.isspace():
        special_count += 1
print("Special character count:", special_count)
