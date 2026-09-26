# write a python program to Check if a string contains only alphabets
def only_alphabets(s):
    return s.isalpha() if s else False
print(only_alphabets('amar4'))
print(only_alphabets('amar'))
