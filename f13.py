# write a python program to Check if a string contains only whitespace
def only_whitespace(s):
    return s.isspace() if s else False
print(only_whitespace('    '))
print(only_whitespace('  d  '))

