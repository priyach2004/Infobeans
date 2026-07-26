'''
2. Space Counter in Chat Messages

A chat application wants to calculate how many spaces are used in a message.

Input: Enter chat message: Good morning everyone how are you

Output: Total spaces: 5
'''

s=input("Enter chat message: ")
count = 0
i=0
while i<len(s):
    if s[i]==" ":
        count += 1
    i+=1
print(f"Total spaces: {count}")