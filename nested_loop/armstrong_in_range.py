'''
4. Armstrong Number Finder

A digital number analysis system checks for Armstrong numbers within a range.
The user enters starting and ending numbers.
The system finds all Armstrong numbers using nested loops.

Input:
Enter starting number: 1
Enter ending number: 500

Output:
Armstrong Numbers are:
1
153
370
371
407
'''

n1 = int(input("Enter starting number: "))
n2 = int(input("Enter ending number: "))
for n in range(n1,n2+1):
    if n<10:
        continue
    num=n
    l = len(str(n))
    sum=0
    while num>0:
        d=num%10
        sum = sum+(d**l)
        num = num//10
    if sum==n:
        print(n)