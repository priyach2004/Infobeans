'''
5. Equilibrium Index Finder

Scenario

Find an index where:

# Sum of elements on the left side

Sum of elements on the right side

Requirements

* Read N and list elements from user
* Find equilibrium index
* If not found, display message

Test Case 1

Input:
[1, 3, 5, 2, 2]

Output:
Equilibrium Index = 2

Explanation:
1 + 3 = 2 + 2

Test Case 2

Input:
[1, 2, 3]

Output:
No Equilibrium Index Found

'''

arr=list(map(int,input("Enter Elements: ").split()))
n=len(arr)
index=-1
for i in range(1,n-1):
    left_sum=0
    right_sum=0
    for j in range(i+1,n):
        right_sum+=arr[j]
    for j in range(i):
        left_sum+=arr[j]
    if right_sum==left_sum:
        index=i
        break
if index!=-1:
	print(f"Equilibrium Index = {index}")
else:
	print("No Equilibrium Index Found")