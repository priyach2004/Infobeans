'''
4.
Find common elements in three sorted arrays.
Given three arrays sorted in increasing order. Find the elements that are common in all three arrays.
Note: can you take care of the duplicates without using any additional Data Structure?
Example 1:
Input:
n1 = 6; A = {1, 5, 10, 20, 40, 80}
n2 = 5; B = {6, 7, 20, 80, 100}
n3 = 8; C = {3, 4, 15, 20, 30, 70, 80, 120}
Output: 20 80
Explanation: 20 and 80 are the only
common elements in A, B and C.
'''

arr1=list(map(int,input("Enter elements in 1st array: ").split()))
arr2=list(map(int,input("Enter elements in 2st array: ").split()))
arr3=list(map(int,input("Enter elements in 3st array: ").split()))

for i in arr1:
    found=0
    for j in arr2:
        if i==j:
            found=1
            break
    if found==1:
        for j in arr3:
            if i==j:
                print(i)
                break