'''
2. Smallest Digit in Number
A manufacturing company prints serial numbers on products. During quality testing, the scanner needs to detect the smallest digit in the serial number to verify coding standards.
Write a program to find the smallest digit in a number using loops.

Input:
57294

Output:
Smallest Digit = 2
'''

n = int(input("Enter a number: "))
a = 10
for i in range(len(str(n))):
	i = n%10
	n = n//10
	if(a>i):
		a = i
print(f"Smallest Digit: {a}")

'''
n = int(input("Enter a number: "))
a = 10
while n>0:
	i = n%10
	n = n//10
	if(a>i):
		a = i
print(f"Smallest Digit: {a}")
'''