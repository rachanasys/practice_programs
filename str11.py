#write a python program to Check if a string contains only uppercase letters using recursion
def only_uppercase(s):
    if not s:
        return True
    if not (s[0].isalpha() and s[0].isupper()):
        return False
    return only_uppercase(s[1:])
print(only_uppercase('Good'))
print(only_uppercase('GOOD'))
