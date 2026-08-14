'''
2.Employee Salary Processing
Store employee salaries in a List and calculate details.

Requirements:

Store salaries
Find average salary
Display salaries greater than average
Remove salaries below 15000

Test Cases:

Input: [10000, 20000, 30000] → Average = 20000, Above Average = 30000
Input: [15000, 15000, 15000] → Average = 15000
Input: [5000, 7000] → Remaining List = []
'''

n=int(input("Enter number of salaries: "))
salary=[]
for i in range(n):
    x = int(input("Enter Salary: "))
    salary.append(x)
print(salary)
sum=0
for i in salary:
    sum+=i
avg=sum/n
print("Above Average: ")
for i in salary:
    if i>avg:
        print(i,end="")
print()
print("Salaries Above 15000: ")
for i in salary:
    if i>15000:
        print(i,end=" ")