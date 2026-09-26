#97 Write a python program to Count frequency of words in a sentence using dictionary.
sentence = "python code is clean code"
word_frequency = {}
for word in sentence.split():
    word_frequency[word] = word_frequency.get(word, 0) + 1
print("Word entry frequency tracking mapping:", word_frequency)
