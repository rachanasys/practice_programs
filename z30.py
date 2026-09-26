# Write a python program to copy a dictionary
original_dict = {"x": 10, "y": 20}
copied_dict = {key: value for key, value in original_dict.items()}
print("Copied dictionary instance:", copied_dict)
