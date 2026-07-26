'''
4. Airline Ticket Pricing Engine

An airline calculates ticket price based on class, distance, and booking time.

If class is business, then check distance. If distance is greater than 1000, price is 8000; otherwise 5000.

If class is economy, then check distance. If distance is greater than 1000, then check booking time. If booking is early, price is 4000; otherwise 5000. If distance is less than or equal to 1000, price is 2500.

Input:
Class = economy
Distance = 1200
Booking = early

Output:
Ticket Price = 4000
'''

clas = input("Class(business/economy): ")
dist = int(input("Distance: "))
booking=input("Booking(early/not early): ")
price=0
if clas.lower()=="business":
	if dist>1000:
		price = 8000
	else:
		price = 5000
		
elif clas.lower()=="economy":
	if dist>1000:
		if booking.lower()=="early":
			price=4000
		else:
			price=5000
	else:
		price=2500
print(f"Ticket Price = {price}")