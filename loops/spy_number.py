'''
4. Spy Number Detector

A cybersecurity system flags special numeric codes.

A number is called a Spy Number if:
Sum of digits = Product of digits

Write a program to check whether the entered number is Spy Number or Not.

Input:
1124

Output:
Spy Number
'''

n=int(input("Enter number: "))
sum=0
prod = 1
while n>0:
	d=n%10
	sum+=d
	prod *= d
	n=n//10
if prod==sum:
	print("Spy Number")
else:
	print("Not a spy number")