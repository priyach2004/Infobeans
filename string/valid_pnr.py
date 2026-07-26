'''
6. Railway Ticket PNR Analyzer

A railway department wants to verify whether a PNR number is valid.

Conditions:
- PNR must start with "PNR"
- Total length should be 12 characters
- Remaining characters should be digits

Input:
Enter PNR: PNR123456789

Output:
Valid PNR Number

'''

s=input("Enter PNR: ")
length = len(s)
x=0
if s[0]=='P' and s[1]=='N' and s[2]=='R' and length==12:
	i=3
	while i<length:
		if s[i] not in "1234567890":
			x=1
			break
		i+=1
	if x==1:
		print("Invalid PNR Number")
    else:
        print("Vali")
else:
	print("Invalid PNR Number")