'''
4.  Instant Messaging Word Encryption System

A messaging application wants to temporarily encrypt messages during
transmission. The encryption rule is to reverse every word individually
while keeping the word positions unchanged.

Input: Enter message: java is powerful

Output: Encrypted Message: avaj si lufrewop
'''

s=input("Enter message: ")      # java is powerful
i=0
result=""
while i<len(s):
    j=i
    while s[j]!=" ":
        j+=1
    word = ""
    c=j
    while j>i:
        j-=1
        word = word+s[j]    
    result = result+" "+word
    i=c+1
print(f"Encrypted Message:{result}")