'''
6. Next Prime Cabin Number Generator

A luxury hotel gives only prime numbered cabins to VIP guests.
Manager enters the last allotted cabin number.
System must find the next available prime cabin number.

Write a program using loops.

Input:
24

Output:
Next Prime Cabin = 29
'''


import  math
n = int(input("Enter a number: "))
num=n+1
isPrime=False
while not isPrime:
    i = 2
    while i<=int(math.sqrt(num)):
        if num%i == 0:
            num=num+1
            break
        i=i+1
    else:
        isPrime = True
print(num)