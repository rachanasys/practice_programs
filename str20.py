#write a python program to check if a string contains all vowels using recursion 
def contains_all_vowels_rec(s, vowels_left=None):
    if vowels_left is None:
        vowels_left = set('aeiou')
    if not vowels_left:
        return True
    if not s:
        return False
    char = s[0].lower()
    return contains_all_vowels_rec(s[1:], vowels_left - {char} if char in vowels_left else vowels_left)
print(contains_all_vowels_rec('amar'))
print(contains_all_vowels_rec('education'))
