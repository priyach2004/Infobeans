'''
10. Student ID Validity Checker (Count Odd Digits)
A school management system assigns numeric IDs to students. The administration wants to verify IDs by checking how many odd digits are present in each ID number. IDs with more odd digits are sent for manual review.

Write a program to count the number of odd digits in a given student ID using loops.

Input:
572943

Output:
Odd Digits Count = 3
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