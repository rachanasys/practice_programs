#write a python program to check if a string contains both vowels and consonants using recursion 
def both_vowels_and_consonants(s, has_vowel=False, has_consonant=False):
    if has_vowel and has_consonant:
        return True
    if not s:
        return False
    if s[0].isalpha():
        if s[0].lower() in 'aeiou':
            has_vowel = True
        else:
            has_consonant = True
    return both_vowels_and_consonants(s[1:], has_vowel, has_consonant)
print(both_vowels_and_consonants('amar'))
print(both_vowels_and_consonants('mrs'))
