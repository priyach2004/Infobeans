'''
7.
 Prime Sum Lucky Number

A lottery app checks if sum of digits is prime.

Write a program to:

- Find sum of digits
- If prime print Lucky Number
- Else Normal Number

Input:
4528

Output:
Sum = 19
Lucky Number
'''

import  math
n = int(input("Enter a number: "))
sum=0
while n>0:
	d=n%10
	sum += d
	n = n//10
print(f"Sum = {sum}")
if sum<=1:
	print("Normal Number")
else:
    i=2
    while i<=int(math.sqrt(sum)):
        if sum%i==0:
            print("Normal Number")
            break
        i = i+1
    else:
        print("Lucky Number")