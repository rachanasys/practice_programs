# write a python program to Check if a string contains both letters and digits
def both_letters_and_digits(s):
    has_letter = any(char.isalpha() for char in s)
    has_digit = any(char.isdigit() for char in s)
    return has_letter and has_digit
print(both_letters_and_digits('member'))
print(both_letters_and_digits('member1'))

