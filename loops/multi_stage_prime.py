'''
2. Multi Stage Prime Lock System

A smart locker opens only if final derived number is prime.

Write a program to:

- Find sum of digits
- Find product of digits
- Find difference between product and sum
- Count digits in difference
- Add digit count to difference
- Check whether final result is Prime or Not

Input:
234

Output:
Sum = 9
Product = 24
Difference = 15
Digits = 2
Final Result = 17
Prime
'''

import math
n = int(input("Enter a number: "))
temp = n
sum = 0
prod = 1

while n > 0:
    d = n % 10
    prod = prod*d
    sum += d
    n = n // 10

print(f"Sum: {sum}")
print(f"Product: {prod}")

diff = abs(prod - sum)
print(f"Difference: {diff}")
digCount = len(str(diff))
print(f"Digits: {digCount}")
res = digCount + diff
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