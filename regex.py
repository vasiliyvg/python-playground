import re

str = "my The hexadecimal 0x000000 and the #000000 nummber and definitely THE 0 + 100 + 99 + 120"

print("Found words:")
print(re.findall(r"\w+", str))
print(re.findall(r"^\w+", str))
print(re.findall(r"\w+$", str))

print("Found hexadecimal number:")
print(re.findall(r"0[xX][0-9a-fA-F]+", str))

print("Found color hexadecimal:")
print(re.findall(r"[#][0-9a-fA-F]{6}", str))

print("Remove all characters except letters and numbers:")
print(re.sub(r"[\W_]+", "", str))

print("Replace multiple occurrence of character 'm' by single:")
print(re.sub(r"m{2,}", "m", str))

print("Find all the occurrences of the, The and THE:")
print(re.findall(r"the|The|THE", str))

print("Find all the even numbers between 0 and 99")
print(re.findall(r"\b[\d]{1,2}\b", str))