#96 Write a python program to Count frequency of characters in a string using dictionary.
text = "hello"
frequency_map = {}
for char in text:
    frequency_map[char] = frequency_map.get(char, 0) + 1
print("Character execution frequency tracking mapping:", frequency_map)
