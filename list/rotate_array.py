'''
7. Array Rotation Analyzer

Scenario

Rotate the array K times towards the right.

Requirements

* Read N and list elements from user
* Read K
* Rotate the array
* Display rotated array

Test Case 1

Input:
Array = [1, 2, 3, 4, 5]
K = 2

Output:
[4, 5, 1, 2, 3]

Test Case 2

Input:
Array = [10, 20, 30, 40]
K = 1

Output:
[40, 10, 20, 30]

'''

arr=list(map(int,input("Enter Elements: ").split()))
k=int(input("Enter k: "))
n=len(arr)
for i in range(0,k):
    last=arr[n-1]
    j=n-1
    while j>0:
        arr[j]=arr[j-1]
        j-=1
    arr[0]=last
print("Result : ",arr)

