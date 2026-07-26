'''
8. A warehouse management system needs to identify the highest stock level among six different storage units to prioritize dispatch.
 The system should take the quantity of items stored in six units as input. It should compare all six values using nested conditions
 and determine which unit has the maximum stock. Display the highest stock value among all six units.

Input:
Unit1 = 120
Unit2 = 450
Unit3 = 300
Unit4 = 275
Unit5 = 500
Unit6 = 390

Output:
Highest Stock = 500
'''

unit1,unit2,unit3,unit4,unit5,unit6 = map(int,input("Enter Unit1, Unit2, Unit3, Unit4, Unit5, Unit6: ").split(","))
if unit1>unit2:
	if unit1>unit3:
		if unit1>unit4:
			if unit1>unit5:
				if unit1>unit6:
					print(f"Highest Stock = {unit1}")
				else:
					print(f"Highest Stock = {unit6}")
			else:
				if unit5>unit6:
					print(f"Highest Stock = {unit5}")
				else:
					print(f"Highest Stock = {unit6}")
		else:
			if unit4>unit5:
				if unit4>unit6:
					print(f"Highest Stock = {unit4}")
				else:
					print(f"Highest Stock = {unit6}")
			else:
				if unit5>unit6:
					print(f"Highest Stock = {unit5}")
				else:
					print(f"Highest Stock = {unit6}")
	else:
		if unit3>unit4:
			if unit3>unit5:
				if unit3>unit6:
					print(f"Highest Stock = {unit3}")
				else:
					print(f"Highest Stock = {unit6}")
			else:
				if unit5>unit6:
					print(f"Highest Stock = {unit5}")
				else:
					print(f"Highest Stock = {unit6}")
		else:
			if unit4>unit5:
				if unit4>unit6:
					print(f"Highest Stock = {unit4}")
				else:
					print(f"Highest Stock = {unit6}")
			else:
				if unit5>unit6:
					print(f"Highest Stock = {unit5}")
				else:
					print(f"Highest Stock = {unit6}")
else:
	if unit2>unit3:
		if unit2>unit4:
			if unit2>unit5:
				if unit2>unit6:
					print(f"Highest Stock = {unit2}")
				else:
					print(f"Highest Stock = {unit6}")
			else:
				if unit5>unit6:
					print(f"Highest Stock = {unit5}")
				else:
					print(f"Highest Stock = {unit6}")
		else:
			if unit4>unit5:
				if unit4>unit6:
					print(f"Highest Stock = {unit4}")
				else:
					print(f"Highest Stock = {unit6}")
			else:
				if unit5>unit6:
					print(f"Highest Stock = {unit5}")
				else:
					print(f"Highest Stock = {unit6}")
	else:
		if unit3>unit4:
			if unit3>unit5:
				if unit3>unit6:
					print(f"Highest Stock = {unit3}")
				else:
					print(f"Highest Stock = {unit6}")
			else:
				if unit5>unit6:
					print(f"Highest Stock = {unit5}")
				else:
					print(f"Highest Stock = {unit6}")
		else:
			if unit4>unit5:
				if unit4>unit6:
					print(f"Highest Stock = {unit4}")
				else:
					print(f"Highest Stock = {unit6}")
			else:
				if unit5>unit6:
					print(f"Highest Stock = {unit5}")
				else:
					print(f"Highest Stock = {unit6}")