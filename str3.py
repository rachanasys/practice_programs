#write a python program to Check if a string is a palindrome using recursion
def is_str_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_str_palindrome(s[1:-1])
print('amanda--',is_str_palindrome('amanda'))
print('mom--',is_str_palindrome('mom'))
print('civic--',is_str_palindrome('civic'))
print('rotator--',is_str_palindrome('rotator'))

