#write a python program to Check if a string contains Only special characters using recursion
def only_special_chars(s):
    if not s:
        return True
    # If it is alphanumeric or whitespace, it's not a special character
    if s[0].isalnum() or s[0].isspace():
        return False
    return only_special_chars(s[1:])
print(only_special_chars('!@#_)()'))
print(only_special_chars('!@#_)(8)'))

