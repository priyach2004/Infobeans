'''
4.
Palindrome Number List Checker
Scenario

A system checks lucky numbers which are palindromes.

Requirements
Check palindrome numbers
Store palindrome numbers in list
Count palindrome numbers
Find largest palindrome
Sort palindrome list
Test Cases

Input:
[121, 131, 20, 44, 55, 100]

Output:

Palindromes: [121, 131, 44, 55]
Count: 4
Largest: 131
Sorted: [44, 55, 121, 131]
'''

s=list(map(int,input("Enter Numbers: ").split()))
res=[]
for i in s:
    temp=i
    rev=0
    while i!=0:
        rev=rev*10+i%10
        i=i//10
    if rev==temp:
        res.append(temp)
print("Palindrome List = ",res)
highest=res[0]
smallest=res[0]
count=len(res)
print("Count = ",count)
for i in res:
    if i>highest:
        highest=i
    if i<smallest:
        smallest=i
print("Largest = ",highest)
print("Smallest = ",smallest)
res.sort()
print(res)
