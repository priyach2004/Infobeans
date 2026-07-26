'''

3. Replace Consecutive Duplicate Characters with Single Character
Data Compression System

A cloud storage company wants to reduce unnecessary repeated characters in text logs.

Write a Python program that replaces consecutive duplicate characters with a single occurrence.

Input:
aaabbbccccdddaa
Output:
abcda

'''

s=input("Input: ")
i=1
result=""+s[0]
while i<len(s):
	if result[-1]!=s[i]:
		result = result+s[i]
	i+=1
print(result)