'''
# 7. Enterprise Password Pattern Strength Analyzer

A cybersecurity company wants to validate advanced passwords.

## Conditions:

* Minimum 10 characters
* At least:

  * 1 uppercase letter
  * 1 lowercase letter
  * 1 digit
  * 1 special character
* No consecutive repeating characters
* No spaces allowed

### Input:

text
Pyth@n1234


### Output:

text
Strong Password


### Input:

text
Paaass@12


### Output:

text
Weak Password
'''

s=input("Enter Password: ")
upr=0
lwr=0
digit=0
special=0
space=0
cons=0
for i in range(len(s)-1):
	if 65<=ord(s[i])<=90:
		upr=1
	elif 97<=ord(s[i])<=122:
		lwr=1
	elif s[i] in "1234567890":
		digit=1
	elif s[i]==" ":
		space=1
	else:
		special=1
	if s[i]==s[i+1]:
		cons=1
if upr>=1 and lwr>=1 and digit>=1 and special>=1 and space==0 and cons==0:
	print("Strong password")
else:
	print("Weak Password")