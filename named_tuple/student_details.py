'''

=====================================
QUESTION 2: STUDENT RESULT PROCESSING
=====================================

A training institute wants to manage student records using NamedTuple.

Fields:
roll_no, name, course, marks

Requirements:

1. Read N student records from the user and store them in a list of NamedTuples.

---

2. Display all student details.

---

3. Find and display the topper of the class.

---

4. Count and display the number of students scoring above 80 marks.

---

5. Calculate and display the average marks.

---

6. Accept a course name from the user and display all students enrolled in that course.

---

Test Case:

Input:
Enter number of students: 4

1 Ravi Python 85
2 Anjali Java 78
3 Karan Python 92
4 Pooja Testing 88

Enter course: Python

Expected Output:
Topper:
3 Karan Python 92

Students Above 80:
3

Average Marks:
85.75

Students in Python Course:
1 Ravi Python 85
3 Karan Python 92

'''

from collections import namedtuple
n=int(input("Enter number of students: "))
Student=namedtuple("student",["st_roll_no","st_name","st_course","st_marks"])
stud=[]
for i in range(n):
	print("Enter details: ")
	rollno=int(input("Enter roll number: "))
	name=input("Enter name: ")
	course=input("Enter course: ")
	marks=int(input("Enter marks: "))
	studt=Student(rollno,name,course,marks)
	stud.append(studt)
course_input=input("Enter a course name: ")
high_marks=0
count=0
sum=0
for x in stud:
	print(f"{x.st_roll_no} {x.st_name} {x.st_course} {x.st_marks}")
	if x.st_marks>high_marks:
		high_marks=x.st_marks
	if x.st_marks>=80:
		count+=1
	sum+=x.st_marks
for x in stud:
	if x.st_marks==high_marks:
		print("Topper: ")
		print(f"{x.st_roll_no} {x.st_name} {x.st_course} {x.st_marks}")
print(f"Students  Above 80: {count}")
print(f"Average Marks: {sum/n}")
for x in stud:
	if x.st_course==course_input:
		print(f"{x.st_roll_no} {x.st_name} {x.st_course} {x.st_marks}")