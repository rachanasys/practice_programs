#79. Write a python program to Find the length of a string using recursion.
def recursive_len(s):
    return 0 if not s else 1 + recursive_len(s[1:])
print("String character length count:", recursive_len("structure"))
