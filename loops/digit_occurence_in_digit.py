'''
*11. Count Occurrence of a Digit*
A system logs repeated digits in a number for pattern analysis and reporting.
Write a program to *count how many times a given digit appears in a number using loops*.

Input: Number = 122312, Digit = 2
Output: 3
'''

n,dig = map(int,input("Enter number,digit: ").split(","))
count = 0

'''
for i in range(len(str(n))):
'''

while n>0:
    num = n%10
    if num==dig:
        count+=1
    n = n//10
print(f"Count = {count}")