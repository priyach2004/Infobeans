'''
4. Problem: Sum of Leaders in an Array After Filtering Invalid Data (Python)

Definition

A company collects daily performance scores of employees. However, the dataset may contain invalid entries.

An element is called a leader if:

It is greater than all elements to its right side
The element must be valid, i.e., it should not be:
Negative number
Zero

Rightmost valid element is always considered a leader.

Input Format
First line → integer n
Second line → n space-separated integers

Output Format
Single integer → sum of all valid leader elements
If no valid elements exist → return -1

Rules
Before finding leaders:

Ignore all negative values and zeros
Work only on positive numbers
Then find leaders from the filtered sequence

Test Case 1

Input:
8
16 0 17 4 -3 3 5 2

Processing:
Filtered array:
[16, 17, 4, 3, 5, 2]

Leaders:
[17, 5, 2]

Output:
24

Test Case 2

Input:
6
-1 0 -5 0 -2 -3

Output:
-1

Test Case 3

Input:
5
10 20 30 40 50

Processing:
Filtered array:
[10, 20, 30, 40, 50]

Leaders:
[50]

Output:
50
'''

arr=list(map(int,input("Enter Elements: ").split()))
f_arr=[]
for i in arr:
	if i>0:
		f_arr=f_arr+[i]
peakindex=-1
leader=[]
if len(f_arr)>0:
    n=len(f_arr)
    for i in range(n):
        isLeader=True
        for j in range(i+1,n):
            if f_arr[i]<f_arr[j]:
                isLeader=False
                break
        if isLeader:
            leader.append(f_arr[i])
    print("Leaders: ",leader)
else:
    print(-1)