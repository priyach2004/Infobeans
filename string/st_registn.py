'''

6. Advanced Student Registration Data Processing System

A national university is developing an intelligent registration portal.
Students enter registration codes using uppercase letters, lowercase
letters, digits, and special symbols. Due to inconsistent data entry,
the administration wants the system to standardize and process the
information before storing it.

Conditions: - Ignore all special characters (@ # $ % & * - _) 
			- Separate alphabets and digits 
			- Convert all alphabets to lowercase 
			- Remove duplicate alphabets 
			- Arrange alphabets in ascending order 
			- Arrange digits in descending order 
			- Display alphabets first and digits later 
			- if no digits are found, display “No Digits Found”

Test Case 1 Input: Enter registration code: zBc@638

Output: Result: bcz863

Test Case 2 Input: Enter registration code: 5Br$dE654b

Output: Result: bder6554

Test Case 3 Input: Enter registration code: A9@C3d#6B1a

Output: Result: abcd9631

Test Case 4 Input: Enter registration code: X#X@M2A4x7

Output: Result: amx742

Test Case 5 Input: Enter registration code: r@T#y

Output: Result: rty No Digits Found

'''

s=input("Enter registration code: ")
l=len(s)
i=0
alph=""
dig=""
result = ""
while i<l:
    if 65<=ord(s[i])<=90 or 97<=ord(s[i])<=122:
        if 65<=ord(s[i])<=90:
            alph = alph+chr(ord(s[i])+32)
        else:
            alph = alph + s[i]
    if s[i] in "1234567890":
        dig = dig+s[i]
    i+=1
alph2=sorted(alph)
result=alph2[0]
i=1
while i<len(alph2):
    if alph2[i] not in result:
        result = result+alph2[i]
    i+=1
digits=sorted(dig)
if dig=="":
    print(result+" No Digits Found")
else:
    i=len(digits)-1
    while i>=0:
        result=result+digits[i]
        i-=1
    print(f"Result = {result}")