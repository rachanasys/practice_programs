#write a python program to Check if a string contains only digits using recursion
def only_digits(s):
    if not s:
        return True
    if not s[0].isdigit():
        return False
    return only_digits(s[1:])
print(only_digits('6263'))
print(only_digits('626a'))
