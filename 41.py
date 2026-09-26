#41. Write a python program to read a text file.
with open('example.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    print(lines)  # Outputs: ['Hello, World!\n', 'This is a sample...\n']
#42. Write a python program to Write to a text file.
with open("file.txt", "w") as f:
     f.write("Hello World")
#43. Write a python program to Count words in a file.
with open("file.txt", "r") as f:
    print(len(f.read().split()))
#44. Write a python program to Count lines in a file.
with open("file.txt", "r") as f:
     print(len(f.readlines()))
#45. Write a python program to Copy content from one file to another.
with open("src.txt", "r") as src, open("dst.txt", "w") as dst:
     dst.write(src.read())
