# write a python program to Check if a string is anagram using function 
def is_anagram(s1, s2):
    # Remove spaces and normalize case
    clean_s1 = sorted(s1.replace(" ", "").lower())
    clean_s2 = sorted(s2.replace(" ", "").lower())
    return clean_s1 == clean_s2
print(is_anagram('listen', 'silent'))
print(is_anagram('teacher', 'silent'))

