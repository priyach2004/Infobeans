'''
15. Smart Parking System

A smart parking system charges based on vehicle type and parking duration:

* Bike → ₹10/hour
* Car → ₹20/hour
* Bus → ₹50/hour
  If parking duration exceeds 5 hours, an additional ₹100 penalty is applied.

Write a Python program to calculate total parking fee.

Input:
Enter vehicle type: Car
Enter hours parked: 6

Output:
Total Parking Fee: ₹220
'''

type = input("Enter vehicle type(bike/car/bus): ")
hrs = int(input("Enter hours parked: "))
fee = None
if type.lower()=="bike":
	fee = 10
elif type.lower()=="car":
	fee = 20
else:
	fee = 50
charge = fee*hrs
if hrs>5:
	charge = charge+100
print(f"Total Parking Fee: ₹{charge}")