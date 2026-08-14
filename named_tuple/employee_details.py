'''
=====================================================================
QUESTION 1: EMPLOYEE SALARY ANALYSIS
====================================

A company wants to store employee details and generate salary reports using NamedTuple.

Fields:
emp_id, emp_name, department, salary

Requirements:

1. Read N employee details from the user and store them in a list of NamedTuples.

---

2. Display all employee details.

---

3. Find and display the employee with the highest salary.

---

4. Find and display the employee with the lowest salary.

---

5. Calculate and display the average salary of all employees.

---

6. Accept a department name from the user and display all employees belonging to that department.

---

Test Case:

Input:
Enter number of employees: 4

101 Rahul IT 50000
102 Priya HR 45000
103 Amit IT 70000
104 Neha Finance 60000

Enter department: IT

Expected Output:
Highest Salary Employee:
103 Amit IT 70000

Lowest Salary Employee:
102 Priya HR 45000

Average Salary:
56250.0

Employees in IT Department:
101 Rahul IT 50000
103 Amit IT 70000

'''


from collections import namedtuple
Employee=namedtuple("Emp",["emp_id", "emp_name", "department", "salary"])
employee=[]
n=int(input("Enter number of employee: "))
for i in range(n):
	print("Enter Details: ")
	id=int(input("Enter employee id: "))
	name=input("Enter employee name: ")
	dept=input("Enter department: ")
	sal=int(input("Enter Employee salary: "))
	emp=Employee(id,name,dept,sal)
	employee.append(emp)
dept_input=input("Enter department: ")
print("Employee Details....")
highest_sal=0
lowest_sal=100000000
sum=0
res=[]
for x in employee:
	print(f"{x.emp_id} {x.emp_name} {x.department}  {x.salary}")
	if x.salary>highest_sal:
		highest_sal=x.salary
	if x.salary<lowest_sal:
		lowest_sal=x.salary
	if dept_input==x.department:
		res.append(x)
	sum+=x.salary
for x in employee:
	if x.salary==highest_sal:
		print("Highest Salary  Employee: ")
		print(f"{x.emp_id} {x.emp_name} {x.department} {x.salary}")
	if x.salary==lowest_sal:
		print("Lowest Salary  Employee: ")
		print(f"{x.emp_id} {x.emp_name} {x.department} {x.salary}")
print(f"Average Salary: \n{sum/n}")
print(f"Employees in {dept_input} Department: ")
for x in employee:
	if x.department==dept_input:
		print(f"{x.emp_id} {x.emp_name} {x.department} {x.salary}")