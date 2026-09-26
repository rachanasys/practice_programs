#write a python program to Check if a string is an anagram using recursion
def is_anagram(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    if len(s1) != len(s2):
        return False
    if not s1 and not s2:
        return True
    if s1[0] not in s2:
        return False
    idx = s2.find(s1[0])
    remaining_s2 = s2[:idx] + s2[idx+1:]
    return is_anagram(s1[1:], remaining_s2)
print("listen vs silent ->", is_anagram("listen", "silent"))        # Output: True
print("TRIANGLE vs integral ->", is_anagram("TRIANGLE", "integral")) # Output: True
