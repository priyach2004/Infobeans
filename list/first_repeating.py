'''
2. First Repeating Number

Scenario

A security system logs employee IDs.

Find the first ID that repeats in the list.

Requirements

* Read N and list elements from user
* Find the first repeating number
* If no repeating number exists, display an appropriate message

Test Case 1

Input:
[10, 5, 3, 4, 3, 5]

Output:
First Repeating Number = 3

Test Case 2

Input:
[1, 2, 3, 4]

Output:
No Repeating Number Found

'''

arr=list(map(int,input("Enter Elements: ").split()))
num=-1
n=len(arr)
for i in range(n):
	count=0
	for j in range(n):
		if arr[i]==arr[j]:
			count+=1
	if count!=1:
		num=arr[i]
		break
if num!=-1:
	print(f"First Repeating Number = {num}")
else:
	print("No Repeating Number Found")