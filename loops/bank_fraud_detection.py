'''
6. Banking Fraud Detection System

A bank checks fraud risk based on transaction amount, location, device, and transaction count.

If amount is greater than or equal to 50000, then check location. If location is international, then check device. If device is new, then check transaction count. If transactions are more than 3, mark High Risk (Block); otherwise Medium Risk. If device is not new, mark Medium Risk.

If location is domestic, then check transaction count. If more than 5, mark Medium Risk; otherwise Low Risk.

If amount is less than 50000, then check unusual activity. If yes, then check device. If device is new, mark Medium Risk; otherwise Low Risk. If no unusual activity, mark Safe.

Input:
Amount = 70000
Location = international
Device = new
Transactions = 4

Output:
Risk Level = High Risk (Blocked)
'''

amt = int(input("Amount: "))
loc = input("Location(international/domestic): ")
device = input("Device(new/not new): ")
transaction=int(input("Transaction: "))
level=""
if amt>=50000:
	if loc.lower()=="international":
		if device.lower()=="new":
			if transaction>3:
				level = "High Risk(Blocked)"
			else:
				level = "Medium Risk"
		else:
			level = "Medium Risk"
	else:
		if transaction>5:
			level="Medium Risk"
		else:
			level="Low Risk"
else:
	activity=input("Unusual Activity(yes/no): ")
	if activity.lower()=="yes":
		if device.lower()=="new":
			level="Medium Risk"
		else:
			level="Low Risk"
	else:
		level="Safe"
print(f"Risk Level = {level}")