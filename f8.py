# write a python program to Check if a string contains only digits 
def only_digits(s):
    return s.isdigit() if s else False
print(only_digits('123456'))
print(only_digits('12m456'))
