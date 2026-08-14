'''
4. Longest Consecutive Sequence

Scenario

Find the longest sequence of consecutive numbers present in the list.

Requirements

* Read N and list elements from user
* Find the length of the longest consecutive sequence
* Display the sequence length

Test Case 1

Input:
[100, 4, 200, 1, 3, 2]

Output:
Longest Consecutive Length = 4

Explanation:
Sequence = 1, 2, 3, 4

Test Case 2

Input:
[10, 11, 12, 20]

Output:
Longest Consecutive Length = 3

'''

arr=list(map(int,input("Enter Elements: ").split()))
max_length=0
for i in arr:
    num=i
    length=1
    for j in arr:
        if j==num+1:
            length+=1
            num+=1
        if length>max_length:
            max_length=length
print("Longest Consecutive Length: ",max_length)