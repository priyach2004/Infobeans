'''

2. Find the Most Frequently Occurring Word
News Channel Keyword Analyzer

A news agency analyzes breaking news headlines to identify the most repeated keyword in a report.

Write a Python program to find the word with the highest frequency.

Input:
india won the match and india created history

Output:
india

'''

s=input("Input: ")
words=s.split()
i=0
l_count=0
result=""
while i<len(words):
	word=words[i]
	count=0
	j=0
	while j<len(words):
		if word==words[j]:
			count+=1
		j+=1
	if l_count<count:
		l_count=count
		result=word
	i+=1
print(result)