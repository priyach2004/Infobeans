'''
1. Email Username Validator

A company wants to check whether an employee email username is valid before creating an official account.

Conditions:
- Username should start with a letter
- Username can contain letters, digits, underscore (_)
- No spaces allowed
- Length should be between 5 and 12 characters

Input:
Enter username: ajay_123

Output:
Valid Username
'''

username = input("Enter username: ")
length = len(username)
x=0
if 5<=length<=12 and (65<=ord(username[0])<=90 or 97<=ord(username[0])<=122):
    i=0
    while i<length:
        if username[i] in "1234567890" or username[i]=="_" or 65<=ord(username[i])<=90 or 97<=ord(username[i])<=122:
            i+=1
            continue
        else:
            x=1
            break
        i+=1
    if x==1:
        print("Invalid Username")
    else:
        print("Valid Username")
else:
    print("Invalid Username")