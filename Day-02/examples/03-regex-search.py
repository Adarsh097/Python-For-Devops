import re

text = "The quick brown fox"
pattern = r"brown"

search = re.search(pattern, text)
print(search) # This will print the match object or None
if search:
    print("Pattern found:", search.group())
else:
    print("Pattern not found")
