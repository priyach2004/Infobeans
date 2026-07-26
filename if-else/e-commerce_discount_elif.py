'''
4. E-Commerce Discount Engine

An online shopping platform provides discounts to customers based on their total purchase amount:

* Above ₹5000 → 20% discount
* ₹2000 to ₹5000 → 10% discount
* Below ₹2000 → 5% discount

Write a Python program to calculate the final amount after discount.

Input:
Enter purchase amount: 4500

Output:
Final Amount: ₹4050
'''

amt = int(input("Enter purchase amount: "))
discount = 0
if amt>5000:
	discount = amt*(10/100)
elif 2000<=amt<=5000:
	discount = amt*(10/100)
else:
	discount = amt*(5/100)
print(f"Final Amount: ₹{amt-discount}")