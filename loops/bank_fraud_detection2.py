'''
6. Banking Fraud Detection System

A bank monitors transactions based on amount, location, OTP verification, and account age.

If transaction amount is at least 10000, then check location. If international, then check OTP verification. If verified, allow; otherwise block. If location is domestic, then check if amount is at least 50000. If yes, check account age. If account age is at least 2 years, allow; otherwise flag. If amount is less than 50000, allow. If transaction amount is less than 10000, then check unusual activity. If yes, flag; otherwise allow.

Input:
Transaction Amount = 60000
Location = domestic
Account Age = 1

Output:
Transaction Status = Flagged
'''

amt = int(input("Transaction Amount: "))
loc = input("Location: ")
age = int(input("Account Age: "))
if amt>=10000:
    if loc.lower()=="international":
        otp = input("otp verified(yes/no): ")
        if otp.lower()=="yes":
            print("Transaction Status = Allowed")
    elif loc.lower()=="domestic":
            if loc.lower()=="domestic":
                if amt>=50000:
                    if age>=2:
                        print("Transaction Status = Allowed")
                    else:
                        print("Transaction Status = Flagged")
                elif amt<50000:
                    print("Transaction Status = Allowed")
elif amt<10000:    
    act = input("Unusual Activity(yes/no): ")
    if act.lower()=="yes":
        print("Transaction Status: Flagged")
    else:
        print("Transaction Status: Allowed")	