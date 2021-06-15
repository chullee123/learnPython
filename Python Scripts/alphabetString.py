"""
Assume s is a string of lower case characters.
Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
"""
s = "abcdefghijklmnopqrstuvwxyz"
highest = ""

def getIfNext(s, i, c = ""):
    currentString = s[i]
    c += currentString
    if i+1 >= len(s):
        return c
    nextString = s[i+1]
    if int(ord(currentString)) <= int(ord(nextString)):
        i += 1
        return getIfNext(s, i, c)
    else:
        return c

for i in range(len(s)):
    r = getIfNext(s, i)
    if len(r) > len(highest):
        highest = r

print("Longest substring in alphabetical order is: " + highest)
