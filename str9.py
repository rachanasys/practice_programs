#write a python program to Check if a string contains only alphabets using recursion
def only_alphabets(s):
    if not s:
        return True
    if not s[0].isalpha():
        return False
    return only_alphabets(s[1:])
print(only_alphabets('ahbfJ8'))
print(only_alphabets('ahbfJa'))

