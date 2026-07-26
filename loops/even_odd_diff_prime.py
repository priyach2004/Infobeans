'''
9.Even Odd Difference Prime System

A smart scanner counts even and odd digits.

Write a program to:

- Count even digits
- Count odd digits
- Find difference
- Check whether difference is Prime or Not

Input:
123456

Output:
Even Count = 3
Odd Count = 3
Difference = 0
Not Prime
'''

import math
n = int(input("Enter a number: "))
evenCount=0
oddCount=0
temp=n
while n>0:
	d=n%10
	if d%2==0:
		evenCount += 1
	else:
		oddCount += 1
	n=n//10
diff = abs(evenCount-oddCount)
print(f"Even Count = {evenCount}\nOdd Count = {oddCount}\nDifference = {diff}")
if diff<=1:
	print("Non Prime Number")
else:
    i=2
    while i<=int(math.sqrt(diff)):
        if diff%i==0:
            print("Not Prime Number")
            break
        i = i+1
    else:
        print("Prime Number")