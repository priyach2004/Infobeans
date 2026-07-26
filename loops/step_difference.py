'''
9.
Step Difference Number Analyzer

A mathematics research center studies hidden patterns inside numbers.
For every entered number, the system compares adjacent digits step by step.

Write a program to:

Find the absolute difference between every pair of adjacent digits
Display all step differences
Find the sum of all step differences
Find the largest step difference
If the sum of step differences is divisible by the number of digits, print Balanced Number
Otherwise print Unbalanced Number

Use loops wherever required.

Input:
57294
Output:
Step Differences: 2 5 7 5
Sum = 19
Largest = 7
Unbalanced Number
'''

n = int(input("Enter a number: "))
l=len(str(n))-1
rev=0
while n>0:
    digit = n%10
    rev = rev*10+digit
    n=n//10
sum=0
largest = 0
print("Step Differences: ",end="")
while rev>0:
    f=rev%10
    rev=rev//10
    s=rev%10

    if rev>0:
        diff = abs(f-s)
        print(diff,end=" ")
        sum =sum+diff
    if diff>largest:
        largest=diff
        
print()
print(f"Sum = {sum}")
print(f"Larget = {largest}")
if sum%l==0:
    print("Balanced Number")
else:
    print("Unbalanced Number")