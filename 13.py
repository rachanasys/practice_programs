#13. Write a python program To Count vowels and consonants in a string.
s = "hello"
v = sum(1 for c in s if c.lower() in "aeiou")
print("Vowels:", v, "Consonants:", sum(1 for c in s if c.isalpha()) - v)

