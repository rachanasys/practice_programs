# write a python program to Check if a string contains both vowels and consonants 
def both_vowels_and_consonants(s):
    vowels = set("aeiou")
    has_vowel = any(char.lower() in vowels for char in s if char.isalpha())
    has_consonant = any(char.lower() not in vowels for char in s if char.isalpha())
    return has_vowel and has_consonant
print(both_vowels_and_consonants('amar'))
print(both_vowels_and_consonants('mrs'))