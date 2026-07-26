'''
5.Number Stability Analyzer

A science lab studies whether digits are in increasing order.

Write a program using for-else loop:

- If every next digit is greater than previous print Stable Number
- Else Unstable Number

Input:
12359

Output:
Stable Number
'''

n=int(input("Enter a number: "))
if len(str(n))==1:
    print("Stable Number")
else:
    while n>0:
        first = n%10
        second = ((n%100)-first)/10
        if second<first:
            n=n//10
            continue
        else:
            print("Unstable Number")
            break
    else:
        print("Stable number")