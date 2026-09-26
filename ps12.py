# Write a python program to Check If a character is a special symbol 
char = '$'
if not char.isalnum() and not char.isspace():
    print(f"'{char}' is a special symbol.")
else:
    print(f"'{char}' is not a special symbol.")
