# write a python program to Check if a string contains unique characters
def has_unique_characters(s):
    return len(s) == len(set(s))
print(has_unique_characters('police'))
print(has_unique_characters('polio'))
