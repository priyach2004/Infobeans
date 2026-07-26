'''
11. Railway Ticket Fare System

A railway system calculates ticket fare based on distance and travel class:

* Distance ≤100 km:
  Sleeper → ₹100, AC → ₹200
* Distance 101–500 km:
  Sleeper → ₹300, AC → ₹600
* Distance >500 km:
  Sleeper → ₹500, AC → ₹1000

Write a Python program to calculate ticket fare.

Input:
Enter distance: 350
Enter class: AC

Output:
Total Fare: ₹600
'''

dist = int(input("Enter distance: "))
clas = input("Enter class(sleeper/ac): ")
fare = None
if dist<=100:
	if clas.lower()=="ac":
		fare = 200
	else:
		fare = 100
elif 101<=dist<=500:
	if clas.lower()=="ac":
		fare = 600
	else:
		fare = 300
else:
	if clas.lower()=="ac":
		fare = 1000
	else:
		fare = 500
print(f"Total Fare: ₹{fare}")