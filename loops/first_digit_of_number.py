'''
3. First Digit of Number
A university receives thousands of application IDs. The first digit of each ID represents the department code, so the admission software must read the first digit quickly.
Write a program to find the first digit of a number using loops.

Input:
53892

Output:
First Digit = 5
'''

n = int(input("Enter a number: "))
for i in range(len(str(n))):
	d=n%10
	i += 1
	n=n//10
print(d)

'''
n = int(input("Enter a number: "))
l=len(str(n))
i=0
while i<l:
	d=n%10
	i += 1
	n=n//10
print(d)
'''