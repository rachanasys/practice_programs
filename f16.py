# write a python program to Check if a string contains both upper lowercase letters
def both_upper_lower(s):
    has_upper = any(char.isupper() for char in s)
    has_lower = any(char.islower() for char in s)
    return has_upper and has_lower
print(both_upper_lower('good'))
print(both_upper_lower('Good'))
