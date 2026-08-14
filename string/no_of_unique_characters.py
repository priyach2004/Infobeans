'''

5. Find the Number of Unique Characters in a String

Password Strength Analyzer
A cybersecurity company checks password strength based on the number of unique characters present.
Passwords containing more unique characters are considered more secure.

Write a Python program to count the number of unique characters in a string.

Input:
aabbccdde

Output:
5

'''

'''
s=input("Input: ")   #abcddbccaa
result=s[0]
i=1
while i<len(s):
    j=1
    while j<len(result):
        if s[i]==result[j]:
            break
        j+=1
    else:
        result=result+s[i]
    i+=1
print(f"Number of Unique Characters = {len(result)}")
'''

s=input("Input: ")   #abcddbccaa
result=""
for ch in s:
    if ch not in result:
        result=result+ch
print(f"Number of Unique Characters = {len(result)}")