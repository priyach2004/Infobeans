'''
9. Abundant Number Detector

A financial system analyzes surplus numbers.

An Abundant Number:
Sum of proper factors > number

Write a program to check Abundant Number.

Input:
12

Output:
Abundant Number
'''

n=int(input("Enter number: "))
i=1
sum=0
while i<=(n/2)+1:
	if n%i==0:
		sum += i
	i+=1
if sum>n:
	print("Abundant Number")
else:
	print("Not an Abundant Number")