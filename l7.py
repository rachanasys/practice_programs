# Write a python program to find the largest word in a sentence
sentence = "I love programming in Python"
words = sentence.split()
largest = max(words, key=len)
print("Largest word:", largest)
