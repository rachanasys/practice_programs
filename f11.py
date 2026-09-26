# write a python program to Check if a string contains only uppercase letters
def only_uppercase(s):
    return s.isupper() if s else False
print(only_uppercase('AMAr'))
print(only_uppercase('AMAR'))
