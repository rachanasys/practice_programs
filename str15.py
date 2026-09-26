#write a python program to Check If a string contains both letters and digits using recursion 
def both_letters_and_digits(s, has_letter=False, has_digit=False):
    if has_letter and has_digit:
        return True
    if not s:
        return False
    if s[0].isalpha():
        has_letter = True
    elif s[0].isdigit():
        has_digit = True
    return both_letters_and_digits(s[1:], has_letter, has_digit)
print(both_letters_and_digits("2 members"))
print(both_letters_and_digits("members"))
