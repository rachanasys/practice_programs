# Write a python program to Remove punctuation from a string 
import string
text = "Hello, world! How's it going?"
cleaned_text = ""
for char in text:
    if char not in string.punctuation:
        cleaned_text += char
print("Text without punctuation:", cleaned_text)
