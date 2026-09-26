#write a python program to check if a string contains unique characters using recursion
def has_unique_characters(s, seen=None):
    if seen is None:
        seen = set()
    if not s:
        return True
    if s[0] in seen:
        return False
    seen.add(s[0])
    return has_unique_characters(s[1:], seen)
print(has_unique_characters('mrs'))
print(has_unique_characters('mrss'))
