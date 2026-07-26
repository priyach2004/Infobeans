'''7. Alternate Digit Prime Checker

A math lab adds alternate digits from right side.

Write a program to:

- Find sum of alternate digits
- Check whether sum is Prime or Not

Input:
12345

Output:
Alternate Sum = 9
Not Prime
'''

import  math
n=int(input("Enter a number: "))
sum=0
while n>0:
	d=n%10
	sum += d
	n=n//100
print(f"Alternate Sum = {sum}")
count=2
for i in range(2,int(math.sqrt(sum))+1):
	if sum%i==0:
		count += 1
if count>2:
	print("Not Prime Number")
else:
	print("Prime Number")