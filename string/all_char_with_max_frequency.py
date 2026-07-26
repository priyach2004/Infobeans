'''

4. Find All Characters with Maximum Frequency
Website Traffic Analysis System

A web analytics company tracks user activity symbols in server logs.

The company wants to identify all characters having the maximum frequency in the given string.

Input:
aabbbccddd
Output:
b d

'''

s=input("Input: ")  #aabbbccddd
i=0
freq=0
most_freq=0
result=""
while i<len(s):
    ch=s[i]
    j=i+1
    while j<len(s) and s[j]==ch:
        j+=1
    freq=j-i
    if most_freq<freq:
        most_freq=freq
        result=ch
    elif most_freq==freq:
        result=result+ch
    i=j
print(result)