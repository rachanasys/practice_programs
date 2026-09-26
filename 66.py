#66. Write a python program to Define a function that counts vowels in a string.
def count_vowels_func(s):
    return sum(1 for char in s.lower() if char in 'aeiou')
print("Vowel count in 'Python':", count_vowels_func("Python"))
