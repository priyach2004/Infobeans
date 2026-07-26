'''
7. Vehicle Number Plate Checker

The traffic department wants to validate vehicle registration numbers.

Conditions:
- First 2 characters should be alphabets
- Next 2 should be digits
- Total length should be 10

Input:
Enter vehicle number: MP04AB1234

Output:
Valid Vehicle Number

'''

s=input("Enter vehicle number: ")
length = len(s)
if length==10 and (65<=ord(s[0])<=90 or 97<=ord(s[0])<=122) and (65<=ord(s[1])<=90 or 97<=ord(s[1])<=122) and s[2] in "1234567890" and s[3] in "1234567890":
	print("Valid Vehicle Number")
else:
	print("Invalid vehicle Number")