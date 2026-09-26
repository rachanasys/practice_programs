#write a python program to check If a string contains both upper and lower case using recursion 
def both_upper_and_lower(s, has_upper=False, has_lower=False):
    if has_upper and has_lower:
        return True
    if not s:
        return False
    if s[0].isupper():
        has_upper = True
    elif s[0].islower():
        has_lower = True
    return both_upper_and_lower(s[1:], has_upper, has_lower)
print(both_upper_and_lower('Good'))
print(both_upper_and_lower('good'))
