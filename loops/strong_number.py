'''
4. Strong Number Checker

A digital lock opens only for strong numbers.

A strong number is a number whose sum of factorial of digits equals the number.

Example:
145 = 1! + 4! + 5!

Write a program using loops to check strong number.

Input:
145

Output:
Strong Number
'''

n = int(input("Enter number: "))
temp=n
sum=0
while n>0:
    d=n%10
    fact = 1
    i=1
    while i<=d:
        fact *= i
        i += 1
    sum += fact
    n=n//10
if temp==sum:
    print("Strong Number")
else:
    print("Non Strong number")