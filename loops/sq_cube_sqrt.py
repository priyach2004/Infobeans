'''
print square, cube and square root of all numbers from 1 to N
'''

import math
n=int(input("Enter n: "))
for i in range(1,n+1):
	print(f"Square of {i} = {i*i}")
	print(f"Cube of {i} = {i**3}")
	print(f"Square Root of {i} = {math.sqrt(n)}")