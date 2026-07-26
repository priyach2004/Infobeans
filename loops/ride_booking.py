'''
7. Ride Booking Surge Pricing System

A ride booking app calculates fare multiplier based on demand, time, and distance.

If demand is at least 80, then check time. If peak time, then check distance. If distance is at least 10, apply 2x fare; otherwise 1.5x. If not peak time, then check if demand is at least 90. If yes, 1.8x; otherwise 1.3x. If demand is less than 80, then check if demand is at least 50. If yes, then if peak time, apply 1.2x; otherwise normal fare. If demand is below 50, normal fare.

Input:
Demand = 85
Time = peak
Distance = 12

Output:
Fare Multiplier = 2x Fare
'''

dem = int(input("Demand: "))
time = input("Time(peak/not peak): ")
dist = int(input("Distance: "))
fare=None
if dem>=80:
	if time.lower()=="peak":
		if dist>=10:
			fare = "2x"
		else:
			fare = "1.5x"
	else:
		if dem>=90:
			fare = "1.8x"
		else:
			fare = "1.3x"
elif dem>=50:
	if time.lower()=="peak":
		fare = "1.2x"
	else:
		fare = "normal"
else:
	fare = "normal"
print(f"Fare Multiplier = {fare} Fare")