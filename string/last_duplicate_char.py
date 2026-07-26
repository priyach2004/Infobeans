'''

5. Cybercrime Log Analysis System

A cybersecurity company monitors encrypted login activity stored as character-based security logs.

During investigation, analysts need to identify the last character that repeats in the log sequence.
This helps detect the most recent duplicated activity pattern before a possible security breach.

Write a Python program to find the last repeating character in a given string.

If no repeating character exists, print:

No repeating character found
Input:
abccdbefga
Output:
a

'''

s=input("Input: ")  #abccdbefga
i=0
result=""
while i<len(s):
    ch=s[i]
    freq=0
    j=0
    while j<len(s):
        if s[j]==ch:
            freq+=1
        j+=1
    if freq>1:
        result=ch
    i+=1
if result=="":
    print("No Repeating Characters")
else:
    print(result)
