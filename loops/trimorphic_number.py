'''
8. Trimorphic Number Analyzer

A coding system checks cube-based patterns.

A Trimorphic Number:
Cube of number ends with the same number.

Example:
4³ = 64

Write a program to check Trimorphic Number.

Input:
4

Output:
Trimorphic Number
'''

n = int(input("Enter number: "))
cube = n**3
l=len(str(n))
if cube%(10**l)==n:
	print("Trimorphic Number")
else:
	print("Non Trimorphic number")