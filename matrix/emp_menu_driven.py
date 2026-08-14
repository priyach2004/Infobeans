'''
3.

MATRIX PERFORMANCE EVALUATION SYSTEM

A company records the monthly performance scores of employees in a matrix format. Each row represents an employee and each column represents a month.

The HR department wants a menu-driven application to analyze employee performance.

Menu
1. Find Employee with Highest Total Score
2. Find Month with Lowest Average Score
3. Display Employee-wise Maximum Score
4. Exit
Requirements
Choice 1 – Find Employee with Highest Total Score
Calculate the sum of each row.
Display the employee number having the highest total score.
Choice 2 – Find Month with Lowest Average Score
Calculate the average of each column.
Display the month having the lowest average score.
Choice 3 – Display Employee-wise Maximum Score
Find and display the maximum value present in each row.
Sample Input
10 20 30
40 50 60
25 35 45
Output
Employee 2 has Highest Total Score = 150

Month 1 Average = 25
Month 2 Average = 35
Month 3 Average = 45

Employee 1 Max Score = 30
Employee 2 Max Score = 60
Employee 3 Max Score = 45
'''

while True:
    print("1. Find Employee with Highest Total Score")
    print("2. Find Month with Lowest Average Score")
    print("3. Display Employee-wise Maximum Scor")
    print("4. Exit")
    choice = int(input("Select  from above: "))
    match choice:
        case 1:
            r1=int(input("Enter number of rows for matrix: "))
            c1=int(input("Enter number of columns for matrix: "))
            a=[]
            print("Enter elements in matrix: ")
            for i in range(r1):
                row=[]
                for j in range(c1):
                    row.append(int(input()))
                a.append(row)
            h_sum=0
            res=0
            k=0
            for i in a:
                sum=0
                for j in i:
                    sum+=j
                if h_sum<sum:
                    h_sum=sum
                    res=k
                k+=1
            print(f"Employee {res+1} has Highest Score")
        case 2:
            r1=int(input("Enter number of rows for matrix: "))
            c1=int(input("Enter number of columns for matrix: "))
            a=[]
            print("Enter elements in matrix: ")
            for i in range(r1):
                row=[]
                for j in range(c1):
                    row.append(int(input()))
                a.append(row)
            lowest=1000000
            month=0
            for i in range(c1):
                sum=0
                for j in range(r1):
                    sum+=a[j][i]
                if lowest>sum:
                    lowest=sum
                    month=i
            print(f"Month {month} has lowest average score: {lowest/r1}")
        case 3:
            r1=int(input("Enter number of rows for matrix: "))
            c1=int(input("Enter number of columns for matrix: "))
            a=[]
            print("Enter elements in matrix: ")
            for i in range(r1):
                row=[]
                for j in range(c1):
                    row.append(int(input()))
                a.append(row)
            for i in range(r1):
                highest=0
                for j in range(c1):
                    if highest<a[i][j]:
                        highest=a[i][j]
                print(f"Employee 1 max score = {highest}")
        case 4:
            print("Exiting...")
            break
