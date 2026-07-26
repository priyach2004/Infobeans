'''
1. Triple Operation Prime Verification System

A cybersecurity company generates a security score from entered access code.

Write a program to:

- Find sum of digits of the number
- Reverse the number
- Find absolute difference between original number and reverse
- Add digit sum and difference
- Check whether final result is Prime or Not Prime

Input:
4215

Output:
Sum of Digits = 12
Reverse = 5124
Difference = 909
Final Result = 921
Not Prime
'''

import math
n = int(input("Enter a number: "))
temp = n
sum = 0
rev = 0

while n > 0:
    d = n % 10
    rev = rev * 10 + d
    sum += d
    n = n // 10

print(f"Sum of Digits: {sum}")
print(f"Reverse: {rev}")

diff = abs(temp - rev)
print(f"Difference: {diff}")

res = sum + diff
print(f"Final Result: {res}")

if res <= 1:
    print("Non Prime")
else:
    i = 2
    while i <= int(math.sqrt(res)):
        if res % i == 0:
            print("Non Prime Number")
            break
        i += 1
    else:
        print("Prime Number")
