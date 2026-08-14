'''
8. Majority Element Detector
============================

Scenario

Find an element occurring more than N/2 times.

Requirements

* Read N and list elements from user
* Find majority element
* If not present, display appropriate message

Test Case 1

Input:
[2, 2, 1, 2, 3, 2, 2]

Output:
Majority Element = 2

Test Case 2

Input:
[1, 2, 3, 4]

Output:
No Majority Element Found
'''

arr=list(map(int,input("Enter Elements: ").split()))
n=int(len(arr)/2)
for i in range(len(arr)):
	count=0
	for j in range(len(arr)):
		if arr[i]==arr[j]:
			count+=1
	if count>=n:
		print("Majority Element: ",arr[i])
		break
else:
    print("Majority Element not found")