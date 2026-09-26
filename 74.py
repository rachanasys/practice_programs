#74. Write a python program to Reverse a string using recursion.
def recursive_reverse_str(s):
    return s if len(s) <= 1 else recursive_reverse_str(s[1:]) + s[0]
print("Recursive reverse string output:", recursive_reverse_str("code"))
