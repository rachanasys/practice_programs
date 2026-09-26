#18. Write a python program To Replace vowels with **".
s = "hello"
import re
print(re.sub(r"[aeiouAEIOU]", "**", s))

