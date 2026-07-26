'''
9. Student Attendance Eligibility System

A college determines whether a student is eligible to sit for exams based on attendance percentage:

* 75% and above → Eligible
* 60% to 74% → Eligible with warning
* Below 60% → Not eligible

Write a Python program to check eligibility.

Input:
Enter attendance percentage: 58

Output:
Status: Not Eligible
'''

atd = int(input("Enter attendance percentage: "))
status = None
if atd>=75:
	status = "Eligible"
elif 60<=atd<=74:
	status = "Eligible with warning"
else:
	status = "Not eligible"
print(f"Status: {status}")