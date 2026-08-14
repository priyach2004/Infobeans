'''
4.

=========================================================
        MATRIX DIAGONAL ANALYSIS SYSTEM
=========================================================

Scenario

A security company stores surveillance data in matrix form.
The analyst wants a menu-driven application to examine the
diagonal elements of the matrix and generate reports.

The application should allow the user to:

1. Display Main Diagonal Elements
2. Display Secondary Diagonal Elements
3. Compare Main and Secondary Diagonal Sums
4. Exit

---------------------------------------------------------
Requirements
---------------------------------------------------------

1. Display the following menu repeatedly until the user selects Exit.

   1. Display Main Diagonal Elements
   2. Display Secondary Diagonal Elements
   3. Compare Main and Secondary Diagonal Sums
   4. Exit

2. Read the size of a square matrix from the user.

3. Read all matrix elements from the user.

4. Based on the user's choice:

   Choice 1 - Display Main Diagonal Elements
   -----------------------------------------
   Display all elements present in the main diagonal.

5. Choice 2 - Display Secondary Diagonal Elements
   ----------------------------------------------
   Display all elements present in the secondary diagonal.

6. Choice 3 - Compare Main and Secondary Diagonal Sums
   ---------------------------------------------------
   Calculate the sum of both diagonals and display:

   - Main Diagonal Sum
   - Secondary Diagonal Sum
   - Which diagonal has the greater sum
   - Or whether both sums are equal

7. Choice 4 - Exit
   -----------------------------------------
   Display:
   "Thank You for Using Matrix Diagonal Analysis System"

---------------------------------------------------------
Sample Input/Output
---------------------------------------------------------

Enter size of matrix: 3

Enter matrix elements:

1 2 3
4 5 6
7 8 9

Menu
1. Display Main Diagonal Elements
2. Display Secondary Diagonal Elements
3. Compare Main and Secondary Diagonal Sums
4. Exit

Enter your choice: 1

Output:
Main Diagonal Elements:
1 5 9

---------------------------------------------------------

Enter your choice: 2

Output:
Secondary Diagonal Elements:
3 5 7

---------------------------------------------------------

Enter your choice: 3

Output:
Main Diagonal Sum = 15
Secondary Diagonal Sum = 15
Both Diagonal Sums are Equal

=========================================================

'''

while True:
    print("1. Display Main Diagonal Elements")
    print("2. Display Secondary Diagonal Elements")
    print("3. Compare Main and Secondary Diagonal Sums")
    print("4. Exit")
    choice=int(input("Enter a choice: "))
    match choice:
        case 1:
            n=int(input("Enter size of square matrix: "))
            a=[]
            print("Enter elements in matrix A: ")
            for i in range(n):
                row=[]
                for j in range(n):
                    row.append(int(input()))
                a.append(row)
            print("Main Diagonal Elements: ")
            for i in range(n):
                print(a[i][i],end=" ")
            print()
        case 2:
            n=int(input("Enter size of square matrix: "))
            a=[]
            print("Enter elements in matrix A: ")
            for i in range(n):
                row=[]
                for j in range(n):
                    row.append(int(input()))
                a.append(row)
            print("Secondary Diagonal Elements: ")
            for i in range(n):
                print(a[i][n-1-i],end=" ")
            print()
        case 3:
            n=int(input("Enter size of square matrix: "))
            a=[]
            print("Enter elements in matrix A: ")
            for i in range(n):
                row=[]
                for j in range(n):
                    row.append(int(input()))
                a.append(row)
            m_sum=0
            s_sum=0
            for i in range(n):
                m_sum+=a[i][i]
                s_sum+=a[i][n-1-i]
            print(f"Main Diagonal Sum = {m_sum}")
            print(f"Secondary Diagonal Sum = {s_sum}")
            if m_sum>s_sum:
                print("Main Diagonal has greater sum")
            elif s_sum>m_sum:
                print("Secondary Diagonal has greater sum")
            else:
                print("Both Diagonal Sums are Equal")
        case 4:
            print("Exiting")
            break
