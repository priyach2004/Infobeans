'''
2.

=========================================================
            MATRIX ANALYSIS SYSTEM
=========================================================


A research laboratory stores experimental data in matrix form.
Scientists want a program that can analyze the matrix and provide
different statistics through a menu-driven application.

The application should allow the user to:

1. Count Prime Numbers Row-wise
2. Count Perfect Numbers Column-wise
3. Display Row-wise Sum
4. Exit

---------------------------------------------------------
Requirements
---------------------------------------------------------

1. Display the following menu repeatedly until the user selects Exit.

   1. Count Prime Numbers Row-wise
   2. Count Perfect Numbers Column-wise
   3. Display Row-wise Sum
   4. Exit

2. Read the number of rows and columns from the user.

3. Read all matrix elements from the user.

4. Based on the user's choice:

   Choice 1 - Count Prime Numbers Row-wise
   ---------------------------------------
   Count and display the number of prime numbers present
   in each row of the matrix.

5. Choice 2 - Count Perfect Numbers Column-wise
   --------------------------------------------
   Count and display the number of perfect numbers present
   in each column of the matrix.

   Note:
   A perfect number is a number that is equal to the sum
   of its proper divisors.

   Examples:
   6  = 1 + 2 + 3
   28 = 1 + 2 + 4 + 7 + 14

6. Choice 3 - Display Row-wise Sum
   --------------------------------
   Calculate and display the sum of each row.

7. Choice 4 - Exit
   --------------------------------
   Display:
   "Thank You for Using Matrix Analysis System"

---------------------------------------------------------
Sample Input/Output
---------------------------------------------------------

Menu
1. Count Prime Numbers Row-wise
2. Count Perfect Numbers Column-wise
3. Display Row-wise Sum
4. Exit

Enter your choice: 1

Enter rows: 3
Enter columns: 3

Enter matrix elements:
2 4 5
6 7 8
11 28 13

Output:
Row 1 Prime Count = 2
Row 2 Prime Count = 1
Row 3 Prime Count = 2

---------------------------------------------------------

Menu
1. Count Prime Numbers Row-wise
2. Count Perfect Numbers Column-wise
3. Display Row-wise Sum
4. Exit

Enter your choice: 2

Output:
Column 1 Perfect Number Count = 1
Column 2 Perfect Number Count = 1
Column 3 Perfect Number Count = 0

---------------------------------------------------------

Menu
1. Count Prime Numbers Row-wise
2. Count Perfect Numbers Column-wise
3. Display Row-wise Sum
4. Exit

Enter your choice: 3

Output:
Row 1 Sum = 11
Row 2 Sum = 21
Row 3 Sum = 52

---------------------------------------------------------

Menu
1. Count Prime Numbers Row-wise
2. Count Perfect Numbers Column-wise
3. Display Row-wise Sum
4. Exit

Enter your choice: 4

Output:
Thank You for Using Matrix Analysis System

=========================================================
'''

while True:
    print("1. Count Prime Numbers Row-wise")
    print("2. Count Perfect Numbers Column-wise")
    print("3. Display Row-wise Sum")
    print("4. Exit")
    choice = int(input("Enter a choice: "))
    match choice:
        case 1:
            r1=int(input("Enter number of rows for matrix: "))
            c1=int(input("Enter number of columns for matrix: "))
            a=[]
            print("Enter elements in matrix A: ")
            for i in range(r1):
                row=[]
                for j in range(c1):
                    row.append(int(input()))
                a.append(row)
            row=1
            for i in a:
                p_count=0
                for n in i:
                    j=1
                    count=0
                    while j<=(n/2):
                        if n%j==0:
                            count+=1
                        j+=1
                    if count<2 and n!=1:
                        p_count+=1
                print(f"Prime numbers in row {row} = {p_count}")
                row+=1
        case 2:
            r1=int(input("Enter number of rows for matrix A: "))
            c1=int(input("Enter number of columns for matrix A: "))
            a=[]
            print("Enter elements in matrix: ")
            for i in range(r1):
                row=[]
                for j in range(c1):
                    row.append(int(input()))
                a.append(row)        
            row=0
            for i in range(len(a[row])):
                p_count=0
                for k in range(len(a)):
                    n=a[k][i]
                    j=1
                    sum=0
                    while j<=(n/2):
                        if n%j==0:
                            sum+=j
                        j+=1
                    if sum==n:
                        p_count+=1
                print(f"Perfect numbers in column {row+1} = {p_count}")
                row+=1
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
            row=1
            for i in a:
                sum=0
                for n in i:
                    sum+=n
                print(f"Sum of row {row} = {sum}")
                row+=1
        case 4:
            print("Exiting...")
            break
