import re

text = "apple,banana,orange,grape"
pattern = r","

split_result = re.split(pattern, text)
print("Split result:", split_result)

text2 = "one;two;three;four"
pattern2 = r";"
split_result2 = re.split(pattern2, text2)
print(split_result2[0])