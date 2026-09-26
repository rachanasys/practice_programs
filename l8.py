# Write a python program to Find the smallest word in a sentence
sentence = "I love programming in Python"
words = sentence.split()

smallest = min(words, key=len)
print("Smallest word:", smallest)
