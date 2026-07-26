'''
13. Employee Performance Appraisal System

A company evaluates employees based on performance rating (1–5):

* 5 → 25% salary hike
* 4 → 20% salary hike
* 3 → 10% salary hike
* 2 → 5% salary hike
* 1 → No hike
  If salary is below ₹20000 and rating is 4 or above, an additional ₹2000 bonus is given.

Write a Python program to calculate revised salary.

Input:
Enter salary: 18000
Enter rating: 4

Output:
Revised Salary: ₹23600
'''

salary = int(input("Enter salary: "))
rat = int(input("Enter rating: "))
hike = None
if rat==5:
	hike = 25
elif rat==4:
	hike = 20
elif rat==3:
	hike = 10
elif rat==2:
	hike = 5
else:
	hike = 0
salaryRise = 0
if salary<=20000 and rat>=4:
    salaryRise = 2000
salary = salaryRise+salary+(salary*(hike/100))
print(f"Revised Salary: ₹{salary}")