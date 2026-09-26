#99 Write a python program to Sort a dictionary by values.
unsorted_dict = {"apple": 5, "banana": 2, "cherry": 8}
sorted_pairs = sorted(unsorted_dict.items(), key=lambda item: item[1])
sorted_dict = dict(sorted_pairs)
print("Realigned dictionary ordered chronologically by value fields:", sorted_dict)
