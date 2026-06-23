'''
5. Banking Security System
   A bank validates login attempt:

* If username is "admin" → Valid user
* If password length ≥ 8 → Strong password

Input:
Enter username: admin
Enter password: secure123

Output:
Valid user
Strong password
'''

username = input("Enter username: ")
pswrd = input("Enter password: ")
if username=="admin":
        print("Valid user")
if pswrd=="secure123":       
    print("Strong password")