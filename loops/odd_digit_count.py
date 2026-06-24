'''
*8. Count Odd Digits*
A banking system flags IDs with too many odd digits for further verification.
Write a program to *count the number of odd digits in a given number using loops*.

Input: 123456
Output: Odd digits count = 3
'''

n = int(input("Enter a number: "))
count = 0

'''
for i in range(len(str(n))):
'''

while n>0:
	num = n%10
	n = n//10
	if num%2==1:
		count += 1
print(f"Even digits count: {count}")