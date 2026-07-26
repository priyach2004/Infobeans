'''
5. Palindrome Product Code Checker

A factory wants to identify whether a product code reads the same forward and backward.

Input:
Enter product code: MADAM

Output:
Palindrome Code

Input:
Enter product code: PRODUCT

Output:
Not a Palindrome Code
'''

s=input("Enter product code: ").lower()
length = len(s)
i=0
j=length-1
while i<=j:
	if s[i]==s[j]:
		i+=1
		j-=1
		continue
	else:
		print("Not a Palindrome Code")
		break
else:
    print("Palindrome Code")