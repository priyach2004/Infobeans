'''
8. Find the Second Highest Repeating Character in a String

Social Media Trend Analysis System

A social media company analyzes hashtags and user comments to identify trending character patterns.

The analytics team wants a Python program to find the character with the second highest frequency in a given string.

This helps detect secondary trending patterns in user activity.

Input:

aaabbbbccddeee

Output:

e

Explanation:

b occurs 4 times → highest
e occurs 3 times → second highest

Condition:

Program should work for both uppercase and lowercase letters.
Spaces should be ignored.
If no second highest frequency exists, print:
Second highest repeating character not found
'''

s=input("Enter String: ")
st=""
for i in s:
	if i not in st:
		st=st+i
max_freq=0
sec_max=0
max=""
for ch in st:
    i=0
    freq=0
    while i<len(s):
        if s[i]==ch:
            freq+=1
        i+=1
    if max_freq<freq:
        max_freq=freq
    if freq>sec_max and freq!=max_freq:
        sec_max=freq
        max=ch
print(max)