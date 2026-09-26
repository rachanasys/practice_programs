# write a python program to Check if a number is palindrome using function 
def is_num_palindrome(n):
    s = str(n)
    return s == s[::-1]
print(is_num_palindrome(12321))
print(is_num_palindrome(123))

