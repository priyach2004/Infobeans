'''
5. Student Grade Classification System (Python List Assignment)

A school stores student marks in a list. The system must analyze the marks and generate a *clear performance report*
by grouping students into grade categories.

Write a Python program to:

* Iterate through the list of marks
* Assign grades based on marks:

  * *>= 90 → A*
  * *>= 75 and < 90 → B*
  * *>= 50 and < 75 → C*
  * *< 50 → Fail*
* Store each category in separate lists
* Count students in each category
* Display a *final structured report (important)*

---

## 📌 Output Format (Mandatory)

Your output must be displayed exactly in this format:


===== STUDENT GRADE REPORT =====

A Grade Students   : [list]
B Grade Students   : [list]
C Grade Students   : [list]
Fail Students      : [list]

--------------------------------
A Count   : X
B Count   : X
C Count   : X
Fail Count: X
--------------------------------

Total Students: X


---

 Input

[95, 82, 67, 45, 30]

Output

===== STUDENT GRADE REPORT =====

A Grade Students   : [95]
B Grade Students   : [82]
C Grade Students   : [67]
Fail Students      : [45, 30]

--------------------------------
A Count   : 1
B Count   : 1
C Count   : 1
Fail Count: 2
--------------------------------

Total Students: 5
'''

marks=list(map(int,input("Enter marks: ").split()))
a_list=[]
b_list=[]
c_list=[]
fail_list=[]
for i in marks:
	if i>=90:
		a_list.append(i)
	elif 75<=i<90:
		b_list.append(i)
	elif 50<=i<75:
		c_list.append(i)
	else:
		fail_list.append(i)
print("===== STUDENT GRADE REPORT =====")
print()
print("A Grade Students  : ",a_list)
print("B Grade Students  : ",b_list)
print("C Grade Students  : ",c_list)
print("Fail Students     : ",fail_list)
print()
print("--------------------------------")
print("A Count    : ",len(a_list))
print("B Count    : ",len(b_list))
print("C Count    : ",len(c_list))
print("Fail Count : ",len(fail_list))
print("--------------------------------")
print("Total Students: ",len(marks))