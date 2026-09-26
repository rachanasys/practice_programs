#20. Write a python program To Find the first non repeated character in a string.
s = "swiss"
print(next((c for c in s if s.count(c) == 1), None))

