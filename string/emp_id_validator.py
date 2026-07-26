'''
4.
Employee ID Validator

A company wants to validate employee IDs before storing them in the database.

Conditions:
- ID must start with "EMP"
- Total length should be 8
- Remaining characters should be digits only

Input:
Enter Employee ID: EMP10234

Output:
Valid Employee ID
'''

id = input("Enter Employee ID: ")
length = len(id)
if id[0]=="E" and id[1]=="M" and id[2]=="P" and length==8:
    i=3
    while i<length:
        if id[i] in "1234567890":
            i+=1
            continue
        else:
            print("Invalid Employee ID")
            break
    print("Valid Employee ID")
else:
	print("Invalid Employee ID")