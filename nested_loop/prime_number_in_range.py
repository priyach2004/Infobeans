'''
3. Prime Number Range Checker

A cyber security system generates prime numbers for encryption analysis.
The user enters a starting number and ending number.
The system checks and displays all prime numbers between the given range using nested loops.

Input:
Enter starting number: 10
Enter ending number: 50

Output:
Prime Numbers are:
11
13
17
19
23
29
31
37
41
43
47
'''

n1 = int(input("Enter starting number: "))
n2 = int(input("Enter ending number: "))
for n in range(n1,n2+1):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count += 1
    if count==2:
        print(n)