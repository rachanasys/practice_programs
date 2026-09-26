#write a python program to Check if a string contains only whitespaces using recursion
def only_whitespaces(s):
    if not s:
        return True
    if not s[0].isspace():
        return False
    return only_whitespaces(s[1:])
print(only_whitespaces('      '))
print(only_whitespaces('    m  '))

                                                            