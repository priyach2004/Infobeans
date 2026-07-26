'''
4. Program should work for both uppercase and lowercase letters.

Find the Shortest Word in a Sentence
Telecom SMS Cost Optimization System
A telecom company charges customers based on the length of words used in bulk SMS campaigns.
The company wants to identify the shortest word in every message for analytics purposes.

Write a Python program to find the shortest word from a given sentence.

Input:
Python is very easy to learn

Output:
is

'''

s=input("Input: ")
i=0
small = 100
result=""
while i<len(s):
	j=i
	while j<len(s) and s[j]!=" ":
		j+=1
	length = j-i
	if length<small:
		small = length
		result=s[i:j]
	i=j+1
print(f"Output = {result}")
	