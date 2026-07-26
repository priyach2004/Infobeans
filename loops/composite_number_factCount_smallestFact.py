'''
6. Composite Number Detector – Risk Version

A product company marks composite numbers as risky.

User enters a number.
System must:

- Check Composite or Not
- Count total factors
- Print smallest factor other than 1

Input:
12

Output:
Composite Number
Factors Count = 6
Smallest Factor = 2
'''

import math
n = int(input("Enter a number: "))
s_fact = 0
isComp=False
if n <= 1:
    print("Neither Prime nor Composite")
else:
    i=2
    while i<=math.sqrt(n):
        if n%i==0:
            s_fact = i
            print("Composite Number")
            isComp=True
            break
        i+=1
    else:
        print("Non Composite Number")
if isComp:
    count = 0
    i=1
    while i<=n/2:
        if n%i==0:
            count += 1
        i+=1
    print(f"Factors Count = {count+1}")
    print(f"Smallest Factor = {s_fact}")
else:
    print(f"Factors Count = 2")