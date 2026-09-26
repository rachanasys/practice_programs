# write a python program to Check if a string contains only special characters
def only_special_chars(s):
    if not s:
        return False
    return all(not char.isalnum() and not char.isspace() for char in s)
print(only_special_chars('%^&*'))
print(only_special_chars('%^&*5'))
