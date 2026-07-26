'''

6. Find Occurrence of a Word in a String

Product Review Analysis System

An e-commerce company wants to analyze customer reviews.

The company wants a Python program to count how many times a particular word appears in a review.

Input Sentence:
iphone is good and iphone battery is strong

Word:
iphone

Output:
2

'''

s=input("Input Sentence: ")
word=input("Word: ")
count=0
i=0
while i<len(s):
	j=i
	while j<len(s) and s[j]!=" ":
		j+=1
	word2=s[i:j]
	if word==word2:
		count+=1
	i=j+1
print(f"Count: {count}")