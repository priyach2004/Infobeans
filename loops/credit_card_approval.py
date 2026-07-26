'''
1. Smart Credit Card Approval System

A bank evaluates credit card applications based on income, credit score, employment type, and existing debt.

If income is greater than or equal to 50000, then check credit score. If credit score is greater than or equal to 750, then check debt. If debt is less than 20000, approve Premium Card; otherwise approve Gold Card. If credit score is less than 750, then check employment type. If employment is government and credit score is at least 650, approve Gold Card; otherwise reject.

If income is less than 50000, then check if income is at least 30000 and credit score is at least 700. If yes, approve Silver Card; otherwise reject.

Input:
Income = 45000
Credit Score = 720
Employment = private
Debt = 10000

Output:
Card Type = Silver Card
'''

inc = int(input("Income: "))
score = int(input("Credit Score: "))
emp = input("Employment(private/government): ")
debt = int(input("Debt: "))
card=""
if inc>=50000:
	if score>=750:
		if debt<2000:
			card = "Premium Card"
		else:
			card="Gold Card"
	else:
		if emp.lower()=="government" and score>=650:
			card = "Gold Card"
		else:
			card = "Rejected"
else:
	if inc>=30000 and score>=700:
		card="Silver Card"
	else:
		card="Rejected"
print(f"Card  Type = {card}")