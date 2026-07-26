'''
# 3. Secure Banking Transaction Analyzer

A banking server generates encrypted transaction IDs using letters and digits.

The fraud detection team wants a Python program to find the first digit that does not repeat in the transaction ID.

If no unique digit exists, print:

text
No unique digit found


### Input:

text
A122334455667789


### Output:

text
8
'''

s=input("Input: ")
i=0
while i<len(s):
	if s[i] in "1234567890":
		ch=s[i]
		j=0
		count=0
		while j<len(s):
			if s[j]==ch:
				count+=1
			j+=1
		if count==1:
			print(ch)
			break
	i+=1
else:
    print("No unique digit found")