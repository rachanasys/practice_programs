# Write a python program to reverse a dictionary
my_dict = {"first": 1, "second": 2}
reversed_dict = dict(reversed(list(my_dict.items())))
print("Reversed insertion order dict:", reversed_dict)
