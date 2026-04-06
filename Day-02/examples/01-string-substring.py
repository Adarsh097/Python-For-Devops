text = "Python is awesome"
substring = "is"
if substring in text:
    print(substring, "found in the text")


if "DevOps" not in text:
    print("DevOps not found in the text")

print(text[0:6])  # Output: Python