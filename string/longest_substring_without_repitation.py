'''
1. Find the Longest Substring Without Repeating Characters
Cybersecurity Session Tracking System

A cybersecurity company monitors user session IDs generated during secure login sessions.

To detect suspicious repeated patterns, the company wants a Python program that finds the longest substring containing no repeated characters.

Input:
abcabcbb
Output:
abc

'''

#pwwke

s=input("Enter string: ")
i=0
temp=""
while i<len(s):
    j=i
    res=""
    while j<len(s):
        if s[j] not in res:
            res=res+s[j]
        else:
            break
        j+=1
    if len(res)>len(temp):
        temp=res
    i+=1
print(temp)