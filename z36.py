# Write a python program to Reverse characters in each word of a sentence
sentence = "Hello World"
reversed_chars = " ".join([word[::-1] for word in sentence.split()])
print("Inverted string word characters:", reversed_chars)
