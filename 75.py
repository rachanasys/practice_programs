#75. Write a python program to Check if a string is palindrome using recursion.
def recursive_is_palindrome(s):
    if len(s) <= 1: return True
    return s[0].lower() == s[-1].lower() and recursive_is_palindrome(s[1:-1])
print("Is 'racecar' palindrome? (Recursive):", recursive_is_palindrome("racecar"))
