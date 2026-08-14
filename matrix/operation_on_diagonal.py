'''
8.
MATRIX PATTERN DETECTION SYSTEM

A satellite monitoring center stores signal strengths in matrix form. Engineers want to identify special patterns in the matrix.

Menu
1. Count Even Numbers Above Main Diagonal
2. Count Odd Numbers Below Main Diagonal
3. Display Boundary Elements
4. Exit
Requirements
Choice 1 – Count Even Numbers Above Main Diagonal

Count all even numbers where:

column > row
Choice 2 – Count Odd Numbers Below Main Diagonal

Count all odd numbers where:

row > column
Choice 3 – Display Boundary Elements

Display all elements present on:

First Row
Last Row
First Column
Last Column

without repeating corner elements.

Sample Input
1 2 3
4 5 6
7 8 9
Output
Even Numbers Above Main Diagonal = 2
(2, 6)

Odd Numbers Below Main Diagonal = 1
(7)

Boundary Elements:
1 2 3 6 9 8 7 4

'''

while True:
	print("1. Count Even Numbers Above Main Diagonal")
	print("2. Count Odd Numbers Below Main Diagonal")
	print("3. Display Boundary Elements")
	print("4. Exit")
	choice=int(input("Select any one: "))
	match choice:
		case 1:
			r=int(input("Enter number of rows: "))
			c=int(input("Enter number of columns: "))
			arr=[]
			for i in range(r):
				row=[]
				for j in range(c):
					row.append(int(input()))
				arr.append(row)
			res=[]
			for i in range(r):
				for j in range(c):
					ele=arr[i][j]
					if i<j and ele%2==0:
						res.append(ele)
			print("Even Numbers Above Main Diagonal = ",len(res))
			print(res)
			
		case 2:
			r=int(input("Enter number of rows: "))
			c=int(input("Enter number of columns: "))
			arr=[]
			for i in range(r):
				row=[]
				for j in range(c):
					row.append(int(input()))
				arr.append(row)
			res=[]
			for i in range(r):
				for j in range(c):
					ele=arr[i][j]
					if i>j and ele%2!=0:
						res.append(ele)
			print("Even Numbers below Main Diagonal = ",len(res))
			print(res)
		
		case 3:
			r=int(input("Enter number of rows: "))
			c=int(input("Enter number of columns: "))
			arr=[]
			for i in range(r):
				row=[]
				for j in range(c):
					row.append(int(input()))
				arr.append(row)
			res=[]            
			for i in range(c):
				res.append(arr[0][i])
			for i in range(1,r):
				res.append(arr[i][c-1])
			for i in range(c-2,-1,-1):
				res.append(arr[r-1][i])
			for i in range(r-2,0,-1):
				res.append(arr[i][0])
			print("Boundary Elements: ")
			print(res)
		case 4:
			print("Exitting...")
			break