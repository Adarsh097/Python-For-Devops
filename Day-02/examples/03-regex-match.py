import re

text = "The quick brown fox"
pattern = r"quick"

match = re.match(pattern, text) # This will print the match object or None
if match:
    print("Match found:", match.group())
else:
    print("No match")
