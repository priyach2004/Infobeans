'''
8. Largest Smallest Sum Prime Checker

A number analyzer finds largest and smallest digit.

Write a program to:

- Find largest digit
- Find smallest digit
- Find sum of both
- Check whether sum is Prime or Not

Input:
57294

Output:
Largest = 9
Smallest = 2
Sum = 11
Prime
'''


import math
n = int(input("Enter a number: "))
largest = 0
smallest = 10
while n>0:
	d=n%10
	if largest<d:
		largest = d
	if smallest>d:
		smallest=d
	n=n//10
sum=largest+smallest
print(f"Largest = {largest}\nSmallest = {smallest}\nSum = {sum}")
if sum<=1:
	print("Non Prime Number")
else:
    i=2
    while i<=int(math.sqrt(sum)):
        if sum%i==0:
            print("Not Prime Number")
            break
        i = i+1
    else:
        print("Prime Number")