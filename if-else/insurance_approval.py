'''
1. Insurance Claim Approval System

An insurance company processes claims based on policy age, claim amount, and accident type. 
The approval depends on multiple levels of verification to reduce fraud.

If the policy age is at least 2 years, then check the claim amount. If the claim amount is up to 50000, then check the accident type. If it is minor, approve the claim; otherwise, approve it with inspection. If the claim amount is between 50001 and 200000, then check the accident type. If it is major, approve with investigation; otherwise reject. If the claim amount exceeds 200000, reject. If the policy age is less than 2 years, then check accident type. If minor, reject; otherwise mark as pending review.

Input:
Policy Age = 3
Claim Amount = 120000
Accident Type = major

Output
Claim Status = Approved with Investigation
'''

age = int(input("Enter Policy Age: "))
amt = int(input("Enter Claim Amount: "))
ac_type = input("Enter Accident Type(major/minor): ")
status = None
if age>=2:
    if amt<=50000:
        if ac_type.lower()=="minor":
            status = "Approved"
        else:
            status = "Approved with inspection"
    elif amt<=200000:   #50001<=amt<=200000
            if ac_type.lower()=="major":
                status = "Approved with investigation"
            else:
                status = "Rejected"
    else:
        status = "Rejected"
else:
    if ac_type.lower()=="minor":
        status = "Rejected"
    else:
        status = "Pending Review"
print(f"Claim Status = {status}")