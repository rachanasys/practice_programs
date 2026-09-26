#write a python program to Check if a number is a palindrome using recursion
def is_num_palindrome(n):
    s = str(n)
    def check(string):
        if len(string) <= 1:
            return True
        if string[0] != string[-1]:
            return False
        return check(string[1:-1])
    return check(s)
print(is_num_palindrome(1243421))
print(is_num_palindrome(421))
