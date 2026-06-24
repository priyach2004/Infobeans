'''
6. Armstrong Number (3-digit)
In coding competitions, certain numbers are considered unique. A 3-digit Armstrong number is one where the sum of the cubes of its digits equals the number itself.
Write a program to *check whether a number is an Armstrong number using loops*.

Input: 153
Output: Armstrong
'''

n = int(input("Enter a number: "))
temp = n
sum = 0

'''
for i in range(len(str(n))):
    num = n%10
    sum += num*num*num
    n = n // 10
'''

while n>0:
    num = n%10
    sum += num*num*num
    n = n // 10
if sum==temp:
	print("Armstrong")
else:
	print("Not Armstrong")