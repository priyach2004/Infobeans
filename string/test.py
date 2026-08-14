'''
1.
Mirror Difference Transaction Verification System(3.5 marks)
A multinational banking company processes thousands of daily transaction IDs. To detect suspicious patterns and validate system-generated IDs,
 the security software performs a Mirror Difference Verification Test.
For every entered transaction ID:

Reverse the digits of the transaction ID

Find the absolute difference between the original ID and the reversed ID


Count the total number of digits in the difference


Apply the following conditions using if-elif-else:

If the difference is 0, print Perfect Match


Else if the difference is divisible by 9, print Verified


Else print Rejected


Write a program to automate this verification process using loops and conditional statements.
Input:
4215
Output:
Reverse = 5124Difference = 909Digits = 3Verified
Input:
1221
Output:
Reverse = 1221Difference = 0Digits = 1Perfect Match
Input:
1234
Output:
Reverse = 4321Difference = 3087Digits = 4Verified
'''

n=int(input("Number: "))
temp=n
rev=0
i=0
while n!=0:
	r=n%10
	rev=(rev*10)+r
	n=n//10
diff=abs(temp-rev)
dig=len(str(diff))
print(f"Reverse = {rev} Difference = {diff} Digits={dig}")
if diff==0:
	print("Perfect Match")
elif diff%9==0:
	print("Verified")
else:
	print("Rejected")












'''
2.
Step Difference Number Analyzer(3.5 marks)

A mathematics research center studies hidden patterns inside numbers.
For every entered number, the system compares adjacent digits step by step.

Write a program to:

Find the absolute difference between every pair of adjacent digits
Display all step differences
Find the sum of all step differences
Find the largest step difference
If the sum of step differences is divisible by the number of digits, print Balanced Number
Otherwise print Unbalanced Number

Use loops wherever required.

Input:
57294
Output:
Step Differences: 2 5 7 5
Sum = 19
Largest = 7
Unbalanced Number
'''


'''
n=int(input("Enter number: "))
real=n
temp=n
rev=0
i=0
while n!=0:
	r=n%10
	rev=(rev*10)+r
	n=n//10
print("Step Differences: ",end="")
sum=0
largest=0
while (rev//10)!=0:
    a=rev%10
    rev=rev//10
    b=rev%10
    diff=abs(a-b)
    print(diff,end=" ")
    sum=sum+diff
    if largest<diff:
        largest=diff
print(f"Sum = {sum}")
print(f"Largest = {largest}")
if sum%(len(str(real)))==0:
    print("Balanced Number")
else:
    print("Unbalanced Number")
'''










'''
3.
Reverse Sentence + Reverse Each Word(3 marks)

Secret Military Communication Decoder
A defense organization stores highly confidential messages in encrypted form.
To decode the message:

1. Reverse the entire sentence.
2. Reverse every individual word.
3. Store the final result back into the original string variable.

You must use the split() method.
Input:

```
Python is powerful
```

Output:

```
lufrewop si nohtyP
```

'''

'''
s=input("Enter a string: ")
st=s.split()
result=""
i=0
while i<len(st):
	res=""
	word=st[i]
	j=len(word)-1
	while j>=0:
		res=res+st[i][j]
		j-=1
	result=res+" "+result
	i+=1
s=result
print(s)
'''


