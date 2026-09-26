#write a python program to check if a string contains repeated characters using recursion 
def has_repeated_characters(s, seen=None):
    if seen is None:
        seen = set()
    if not s:
        return False
    if s[0] in seen:
        return True
    seen.add(s[0])
    return has_repeated_characters(s[1:], seen)
print(has_repeated_characters('mrs'))
print(has_repeated_characters('mrss'))
