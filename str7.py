#write a python program to Check if a string is a pangram using recursion
def is_pangram(s, alphabet=None):
    if alphabet is None:
        alphabet = set("abcdefghijklmnopqrstuvwxyz")
    if not alphabet:
        return True
    if not s:
        return False
    char = s[0].lower()
    return is_pangram(s[1:], alphabet - {char} if char in alphabet else alphabet)
sentence1 = "The quick brown fox jumps over the lazy dog"
print("Test 1 (Classic Pangram) ->", is_pangram(sentence1))
sentence3 = "The quick brown fox jumps over the lazy do"
print("Test 2 (Missing 'g') ->", is_pangram(sentence3))
