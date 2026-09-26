#write a python program to Check if a string contains only alphanumeric characters using recursion
def only_alphanumeric(s):
    if not s:
        return True
    if not s[0].isalnum():
        return False
    return only_alphanumeric(s[1:])
print(only_alphanumeric('ahbfd5a'))
print(only_alphanumeric('ahbfd5*90(a'))

