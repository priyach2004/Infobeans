'''
5. Next Prime ID Generator – Smart Version

A company gives prime numbered employee IDs to premium staff.

Manager enters current ID.
System must:

- Find next prime number after current ID
- Find difference between current ID and next prime

Write a program using loops.

Input:
20

Output:
Next Prime ID = 23
Gap = 3
'''

import  math
n = int(input("Enter a number: "))
if n<=2:
    num=n+1
else:
    num = n+1
    x=0
    while x!=1:
        i=2
        while i<=int(math.sqrt(num)):
            if num%i==0:
                num=num+1
                break
            i = i+1
        else:
            x=1
print(f"Next Prime = {num}")
print(f"Gap = {abs(n-num)}")