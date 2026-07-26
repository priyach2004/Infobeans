'''
7. Adam Number Verification System – Question

A high-security digital system is designed to validate special mirrored numbers known as Adam Numbers before granting access to sensitive data.

When a user enters a numeric code, the system performs a dual verification process:

* It calculates the square of the entered number.
* It reverses the number and calculates the square of the reversed value.
* Finally, it checks whether both results are mirror images (reverses) of each other.

A number is called an Adam Number if:
The square of the number and the square of its reverse are reverses of each other.

Task:
Write a Python program to check whether a given number is an Adam Number or not.

Examples:

Input:
12
Output:
Adam Number

Input:
13
Output:
Not an Adam Number

Input:
11
Output:
Adam Number

Example:
12 → 12² = 144, reverse(12) = 21 → 21² = 441 → reverse of 144
'''

n=int(input("Enter number: "))
temp=n
sq=n**2
rev=0
while n>0:
	d=n%10
	rev = d+(rev*10)
	n=n//10

revSq=rev**2
rev_of_revSq=0

while sq>0:
	d=sq%10
	rev_of_revSq = d+(rev_of_revSq*10)
	sq=sq//10
if revSq==rev_of_revSq:
	print("Adam Number")
else:
	print("Not an Adam Number")