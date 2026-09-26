# write a python program to Check if a string contains repeated characters 
def has_repeated_characters(s):
    seen = set()
    for char in s:
        if char in seen:
            return True
        seen.add(char)
    return False
print(has_repeated_characters('mrs'))
print(has_repeated_characters('mrss'))
