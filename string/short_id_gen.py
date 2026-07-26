'''

2.  Corporate Employee Short ID Generator

A multinational company wants to automatically generate short IDs for
employees while creating official email accounts. The system should take
the employee’s full name and create an ID using the first character of
each word.

Conditions: - Take first character of every word - Convert all
characters to uppercase

Input: Enter employee name: ajay singh thakur

Output: Employee Short ID: AST

'''

s=input("Enter employee name: ")
res=""
i=0
while i<len(s):
	if i==0 or ( s[i-1]==" " and (65<=ord(s[i])<=90 or 97<=ord(s[i])<=122)):
		if 97<=ord(s[i])<=122:
			res=res+chr(ord(s[i])-32)
		else:
			res=res+s[i]
	i+=1
print(f"Employee Short ID: {res}")