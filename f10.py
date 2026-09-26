# write a python program to Check if a string contains only alphanumeric characters
def only_alphanumeric(s):
    return s.isalnum() if s else False
print(only_alphanumeric('rach_123'))
print(only_alphanumeric('rach123'))
