# Write a python program to Reverse elements of a nested list
nested_list = [[1, 2], [3, 4], [5, 6]]
reversed_nested = [sublist[::-1] for sublist in nested_list[::-1]]
print("Inverted nested list framework:", reversed_nested)
