'''
1.
=========================================================
        MATRIX OPERATIONS MANAGEMENT SYSTEM
=========================================================


A data analysis company stores numerical information in matrix form.
To help employees perform matrix-related operations efficiently,
the company wants a menu-driven application.

The application should allow the user to:

1. Add Two Matrices
2. Subtract Two Matrices
3. Compare Two Matrices
4. Exit

The user must enter the number of rows, columns, and all matrix
elements. The program should perform the selected operation and
display the result.

---------------------------------------------------------
Requirements
---------------------------------------------------------

1. Display the following menu repeatedly until the user chooses Exit.

   1. Add Two Matrices
   2. Subtract Two Matrices
   3. Compare Two Matrices
   4. Exit

2. Read the number of rows and columns from the user.

3. Read all elements of Matrix A and Matrix B from the user whenever
   required.

4. Based on the user's choice:

   Choice 1 - Add Two Matrices
   --------------------------------
   Add corresponding elements of both matrices and display
   the resultant matrix.

5. Choice 2 - Subtract Two Matrices
   --------------------------------
   Subtract corresponding elements of Matrix B from Matrix A
   and display the resultant matrix.

6. Choice 3 - Compare Two Matrices
   --------------------------------
   Check whether both matrices are equal.

   Two matrices are considered equal if:
   - They have the same dimensions.
   - Corresponding elements are equal.

   Display:
   "Matrices are Equal"
   or
   "Matrices are Not Equal"

7. Choice 4 - Exit
   --------------------------------
   Display:
   "Thank You for Using Matrix Operations Management System"

---------------------------------------------------------
Sample Input/Output
---------------------------------------------------------

Menu
1. Add Two Matrices
2. Subtract Two Matrices
3. Compare Two Matrices
4. Exit

Enter your choice: 1

Enter number of rows: 2
Enter number of columns: 2

Enter Matrix A:
1 2
3 4

Enter Matrix B:
5 6
7 8

Result Matrix:
6 8
10 12

---------------------------------------------------------

Menu
1. Add Two Matrices
2. Subtract Two Matrices
3. Compare Two Matrices
4. Exit

Enter your choice: 3

Enter number of rows: 2
Enter number of columns: 2

Enter Matrix A:
1 2
3 4

Enter Matrix B:
1 2
3 4

Output:
Matrices are Equal

---------------------------------------------------------

Menu
1. Add Two Matrices
2. Subtract Two Matrices
3. Compare Two Matrices
4. Exit

Enter your choice: 4

Output:
Thank You for Using Matrix Operations Management System

=========================================================

'''

while True:
    print("1. Add two Matrices")
    print("2. Subtract two Matrices")
    print("3. Compare two Matrices")
    print("4. Exit")
    choice = int(input("Enter a choice: "))
    match choice:
        case 1:
            r1=int(input("Enter number of rows for matrix A: "))
            c1=int(input("Enter number of columns for matrix A: "))
            r2=int(input("Enter number of rows for matrix B: "))
            c2=int(input("Enter number of rows for matrix B: "))
            a=[]
            b=[]
            print("Enter elements in matrix A: ")
            for i in range(r1):
                row=[]
                for j in range(c1):
                    row.append(int(input()))
                a.append(row)
            print("Enter elements in matrix B: ")
            for i in range(r2):
                row=[]
                for j in range(c2):
                    row.append(int(input()))
                b.append(row)
            c=[]
            for i in range(r1):
                row=[]
                for j in range(c1):
                    row.append(a[i][j]+b[i][j])
                c.append(row)
            print("Matrix A: ")
            for i in a:
                print(*i)
            print("Matrix B: ")
            for i in b:
                print(*i)
            print("Addition Matrix: ")
            for i in c:
                print(*i)
        case 2:
            r1=int(input("Enter number of rows for matrix A: "))
            c1=int(input("Enter number of columns for matrix A: "))
            r2=int(input("Enter number of rows for matrix B: "))
            c2=int(input("Enter number of rows for matrix B: "))
            a=[]
            b=[]
            print("Enter elements in matrix A: ")
            for i in range(r1):
                row=[]
                for j in range(c1):
                    row.append(int(input()))
                a.append(row)
            print("Enter elements in matrix B: ")
            for i in range(r2):
                row=[]
                for j in range(c2):
                    row.append(int(input()))
                b.append(row)
            c=[]
            for i in range(r1):
                row=[]
                for j in range(c1):
                    row.append(a[i][j]-b[i][j])
                c.append(row)
            print("Matrix A: ")
            for i in a:
                print(*i)
            print("Matrix B")
            for i in b:
                print(*i)
            print("Addition Matrix: ")
            for i in c:
                print(*i)
        case 3:
            r1=int(input("Enter number of rows for matrix A: "))
            c1=int(input("Enter number of columns for matrix A: "))
            r2=int(input("Enter number of rows for matrix B: "))
            c2=int(input("Enter number of rows for matrix B: "))
            a=[]
            b=[]
            print("Enter elements in matrix A: ")
            for i in range(r1):
                row=[]
                for j in range(c1):
                    row.append(int(input()))
                a.append(row)
            print("Enter elements in matrix B: ")
            for i in range(r2):
                row=[]
                for j in range(c2):
                    row.append(int(input()))
                b.append(row)
            c=[]
            flag=0
            for i in range(r1):
                for j in range(c1):
                    if a[i][j]!=b[i][j]:
                        flag=1
                if flag==1:
                    print("Not equal")
                    break
            else:
                print("Matrices are equal")
            print("Matrix A: ")
            for i in a:
                print(*i)
            print("Matrix B")
            for i in b:
                print(*i)
        case 4:
            print("Exiting...")
            break
