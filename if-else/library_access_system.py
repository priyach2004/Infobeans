'''
9. Library Access System
   A library checks:

* If membership is active → Entry allowed
* If books issued < 3 → Can issue more books

Input:
Membership active (yes/no): yes
Books issued: 2

Output:
Entry allowed
Can issue more books
'''

isActive = input("Membership active (yes/no): ")
books = int(input("Books issued: "))
if isActive.lower()=="yes":
        print("Entry allowed")
if books<3:       
    print("Can issue more books")