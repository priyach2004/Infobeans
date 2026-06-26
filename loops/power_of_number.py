'''
7. Power of a Number
A scientific calculator app is used by engineering students for repeated multiplication operations. It should calculate the value of a number raised to a given power.
Write a program to calculate n raised to power p using loops.

Input:
2 5

Output:
32
'''

n1,n2 = map(int,input("Enter a number: ").split(","))
num=1
for i in range(1,n2+1):
	num=num*n1
	i+=1
print(num)

'''
n1,n2 = map(int,input("Enter a number: ").split(","))
i=1
num=1
while i<=n2:
	num=num*n1
	i+=1
print(num)
'''