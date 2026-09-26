# Write a python program to Define a function that checks if a string is a palindrome.
def check_palindrome(s):
    return s.lower() == s.lower()[::-1]
print("Is 'radar' a palindrome?:", check_palindrome("radar"))
