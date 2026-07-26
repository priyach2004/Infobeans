'''
6. Palindrome Number Range Checker

A barcode verification system checks for palindrome numbers within a specific range.
The user enters starting and ending numbers.
The system displays all palindrome numbers using nested loops.

Input:
Enter starting number: 100
Enter ending number: 200

Output:
Palindrome Numbers are:
101
111
121
131
141
151
161
171
181
191
'''

n1 = int(input("Enter starting number: "))
n2 = int(input("Enter ending number: "))
print("Strong Numbers are: ")
for n in range(n1,n2+1):
    num=n
    rev=0
    while num>0:
        d=num%10
        rev=rev*10+d
        num=num//10
    if n==rev:
        print(n)