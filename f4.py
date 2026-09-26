# write a python program to Check if a string is palindrome using function 
def is_str_palindrome(s):
    # Case-insensitive check
    clean_s = s.lower()
    return clean_s == clean_s[::-1]
print(is_str_palindrome('rotator'))
print(is_str_palindrome('room'))
