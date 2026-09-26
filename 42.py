#46. Write a python program to To check if a file exists.
import os
print(os.path.exists("file.txt"))
#47. Write a python program to To append text to a file.
with open("file.txt", "a") as f:
     f.write(" Appended text.")
#48. Write a python program to Find the longest word in a file.
with open("file.txt", "r") as f:
     print(max(f.read().split(), key=len))
#49. Write a python program to Remove blank lines from a file.
with open("file.txt", "r") as f:
     lines = [line for line in f if line.strip()]
with open("file.txt", "w") as f:
     f.writelines(lines)
#50. Write a python program to Read a csv file.
import csv
with open("data.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
                    print(row)
                    