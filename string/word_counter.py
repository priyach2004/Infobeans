'''
3. Word Counter in Complaint Message

A customer care system wants to count how many words are present in a complaint message.

Input:
Enter complaint: Delivery was delayed again today

Output:
Total words: 5
'''

msg = input("Enter complaint: ")
length = len(msg)
count = 0
i=0
while i<length:
	if i==0 or (msg[i-1]==" " and msg[i]!=" "):
		count+=1
	i+=1
print(f"Total Words: {count}")