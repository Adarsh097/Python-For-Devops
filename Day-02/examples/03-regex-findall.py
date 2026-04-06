import re

text = "The quick brown fox"
pattern = r"brown"

search = re.search(pattern, text)
if search:
    print("Pattern found:", search.group())
else:
    print("Pattern not found")


pattern2 = r"fx"
search2 = re.search(pattern2, text)
if search2:
    print("Pattern found:", search2.group())
else:
    print("Pattern not found")