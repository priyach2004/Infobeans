'''
4. Prime Security Code Checker – Advanced

A high-security lab accepts only prime numbered access codes.

When a user enters a number, the software must:

- Check whether number is prime
- If prime, print next immediate prime number
- If not prime, print previous immediate prime number

Write a program using loops only.

Input:
29

Output:
Prime Number
Next Prime = 31
'''

import math
n = int(input("Enter a number: "))

isPrime = False
if n <= 1:
    print("Non Prime Number", "\n", "Previous Prime = None")
 
else:
    i = 2
    while i <= int(math.sqrt(n)):
        if n % i == 0:
            print("Non Prime Number")
            break
        i = i + 1
    else:
        print("Prime Number")
        isPrime = True

if isPrime:
    num = n + 1
    x = 0
    while x != 1:
        i = 2
        while i <= int(math.sqrt(num)):
            if num % i == 0:
                num = num + 1
                break
            i = i + 1
        else:
            x = 1
    print("Next Prime:", num)

else:
    num = n - 1
    if n <= 1:
        num = 2
    else:
        num = n - 1
        x = 0
        while x != 1:
            i = 2
            while i <= int(math.sqrt(num)):
                if num % i == 0:
                    num = num - 1
                    break
                i = i + 1
            else:
                x = 1
    print("Previous Prime:", num)
