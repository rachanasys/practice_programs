# Write a python program to Generate a random password
import random
import string
password = "".join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=12))
print("Random secure password:", password)
