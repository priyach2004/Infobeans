'''
5. Advanced Password Security Checker

A cyber security company wants to verify whether employee passwords are highly secure before giving system access.

Conditions: Password must:

Start with an uppercase letter
End with a digit
Contain at least 2 digits
Contain at least 1 special character (@ # $ % & *)
Must not contain spaces
Length should be between 8 and 15 characters

Input: Enter password: Python@45

Output: Secure Password

'''

s = input("Enter password: ")
length = len(s)
dig = 0
special = 0
space = 0
if 8<=length<=15 and 65 <= ord(s[0]) <= 90 and s[length-1] in "1234567890":
    i = 0
    while i < length:
        if s[i] in "1234567890":
            dig += 1
        elif s[i] == " ":
            space += 1
        elif s[i] in "@#$%&*":
            special += 1
        i += 1
    if dig >= 2 and special >= 1 and space == 0:
        print("Secure Password")
else:
    print("Not secured password")
