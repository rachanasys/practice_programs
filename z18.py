# Write a python program to Generate a random alphanumeric string
import random
import string
alphanumeric_str = "".join(random.choices(string.ascii_letters + string.digits, k=10))
print("Random alphanumeric string:", alphanumeric_str)
