"""Assume s is a string of lower case characters.
Write a program that prints the number of times the string 'bob' occurs in s."""
bobCount = 0
s = 'spboobaobooxgobooloboborbobobbobobnwoobobo'
for i in range(len(s)):
    if i+3 > len(s):
        break
    if s[i] == "b" and s[i+1] == "o" and s[i+2] == "b":
        bobCount += 1

print("Number of times bob occurs is: " + str(bobCount))

