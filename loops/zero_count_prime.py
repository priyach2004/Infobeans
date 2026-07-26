'''
10.Zero Count Prime Scanner

A banking system checks account numbers.

Write a program to:

- Count zero digits
- Find sum of digits
- Add zero count and sum
- Multiply by smallest digit
- Check whether final result is Prime or Not

Input:
908406

Output:
Zero Count = 2
Sum = 27
Smallest Digit = 0
Final Result = 0
Not Prime
'''

import math
n = int(input("Enter number: "))
zero=0
sum = 0
s_digit=10
while n>0:
	d=n%10
	if d==0:
		zero += 1
	sum += d
	if s_digit>d:
		s_digit = d
	n=n//10
res = s_digit*(zero+sum)
print(f"Zero Count = {zero}")
print(f"Sum = {sum}")
print(f"Smallest Digit = {s_digit}")
print(f"Final Result = {res}")
if res<=1:
	print("Non Prime Number")
else:
    i=2
    while i<=int(math.sqrt(res)):
        if res%i==0:
            print("Not Prime Number")
            break
        i = i+1
    else:
        print("Prime Number")