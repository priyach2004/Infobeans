'''
# 6. AI Chat Toxic Pattern Detector

An AI moderation system wants to detect whether a sentence contains three consecutive repeating characters.

If found:
text
Spam Pattern Found
Else:
text
Clean Message

### Input:

text
heyyy broooo welcome

### Output:

text
Spam Pattern Found
'''

s=input("Input: ")
i=0
while i<len(s):
	ch=s[i]
	j=i
	count=0
	while j<len(s) and s[j]==s[i]:
		count+=1
		j+=1
	if count>=3:
		print("Spam Pattern Found")
		break
	i+=1
else:
	print("Clean Message")