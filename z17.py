# Write a python program to Generate a random string of given length
import random
import string
length = 8
random_str = "".join(random.choices(string.ascii_letters, k=length))
print(f"Random string of length {length}:", random_str)
        