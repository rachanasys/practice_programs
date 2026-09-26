#write a python program to Check if a string contains only lowercase letters using recursion
def only_lowercase(s):
    if not s:
        return True
    if not (s[0].isalpha() and s[0].islower()):
        return False
    return only_lowercase(s[1:])
print(only_lowercase('good'))
print(only_lowercase('GOOD'))

