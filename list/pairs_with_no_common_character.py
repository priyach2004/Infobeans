'''
2.
Secure Password Analysis

A cybersecurity team wants to identify pairs of passwords having no common characters.

Problem Statement:

Given N strings, count the number of pairs that do not share any common character.

Example:

Input

N = 4
passwords[] = {"abc", "de", "fg", "ad"}

Output

3

Explanation

("abc","de")
("abc","fg")
("de","fg")
'''

arr=list(input("Enter elements: ").split())
count=0
for m in range(len(arr)):
    i=arr[m]
    for n in range(m+1,len(arr)):
        j=arr[n]
        k=0
        while k<len(i):
            if i[k] in j:
                break
            k+=1
        else:
            count+=1
print("Count = ",count)