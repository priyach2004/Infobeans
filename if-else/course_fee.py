'''
14. Online Course Fee System

An online platform offers courses with fixed fees:

* Programming → ₹5000
* Design → ₹4000
* Marketing → ₹3000
  Discount is applied based on user type:
* Student → 20% discount
* Working Professional → 10% discount
* Others → No discount

Write a Python program to calculate final course fee.

Input:
Enter course category: Programming
Enter user type: Student

Output:
Final Course Fee: ₹4000
'''

course = input("Enter course category(programming/design/marketing): ")
usertype = input("Enter user type(student/working professional/other): ")
fee = None
if course.lower()=="programming":
	fee=5000
elif course.lower()=="design":
	fee=4000
else:
	fee=3000
if usertype.lower()=="student":
	fee = fee-(fee*(20/100))
elif usertype.lower()=="working professional":
	fee = fee-(fee*(10/100))
print(f"Final Course Fee: ₹{fee}")