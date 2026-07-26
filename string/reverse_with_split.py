'''

2. Reverse Sentence + Reverse Each Word

Secret Military Communication Decoder
A defense organization stores highly confidential messages in encrypted form.
To decode the message:

1. Reverse the entire sentence.
2. Reverse every individual word.
3. Store the final result back into the original string variable.

You must use the split() method.

Input:
Python is powerful
Output:
lufrewop si nohtyP

'''

s=input("Input: ")
word = s.split()
i=len(word)-1
result=""
while i>=0:
	j=len(word[i])-1
	while j>=0:
		result=result+word[i][j]
		j-=1
	result=result+" "
	i-=1
print(f"Output: {result}")