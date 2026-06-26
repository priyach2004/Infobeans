'''
1. Largest Digit in Number
A cybersecurity company checks numeric passwords used in smart lockers. To identify password strength, the system finds the highest digit present in the entered password. Higher digits indicate stronger variation in the password pattern.
Write a program to find the largest digit in a number using loops.

Input:
57294

Output:
Largest Digit = 9
'''

n = int(input("Enter a number: "))
a = 0
for i in range(len(str(n))):
	i = n%10
	n = n//10
	if(a<i):
		a = i
print(f"Largest Digit: {a}")

'''
n = int(input("Enter a number: "))
a = 0
while n>0:
	i = n%10
	n = n//10
	if(a<i):
		a = i
print(f"Largest Digit: {a}")
'''