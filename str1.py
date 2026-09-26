#write a python program to check if a string contains all vowels
def has_all_vowels(s, vowels=None):
    if vowels is None:
        vowels = {'a', 'e', 'i', 'o', 'u'}
    if not vowels:
        return True
    if not s:
        return False
    char = s[0].lower()
    new_vowels = vowels - {char} if char in vowels else vowels
    # Recursively check the rest of the string
    return has_all_vowels(s[1:], new_vowels)

print("education ->", has_all_vowels("education")) 
print("alphabet ->", has_all_vowels("alphabet"))   
print("Empty string ->", has_all_vowels("")) 
