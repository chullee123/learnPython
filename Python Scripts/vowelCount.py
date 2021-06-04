"""
Assume s is a string of lower case characters.
Write a program that counts up the number of vowels contained in the string s.
"""
vowels = 0
s = "erwqiojqjiovdasklmvbnlk"
for char in s:
    if char == "a" or char == "e" or char == "i" or char =="o" \
    or char == "u":
        vowels += 1

print(f"Number of vowels: {vowels}")



