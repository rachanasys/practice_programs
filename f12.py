# write a python program to Check if a string contains only lowercase letters 
def only_lowercase(s):
    return s.islower() if s else False
print(only_lowercase('amar'))
print(only_lowercase('AmaR'))

