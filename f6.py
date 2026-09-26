# write a python program to Check if a string is pangram using function 
def is_pangram(s):
    # Keep only lowercase alphabetic characters and convert to a set
    letters = {char for char in s.lower() if char.isalpha()}
    return len(letters) == 26
print(is_pangram('ananya'))
print(is_pangram('The quick brown fox jumps over the lazy dog'))
