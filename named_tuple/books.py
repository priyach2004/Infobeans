'''

=====================================================================
QUESTION 5: LIBRARY BOOK RECORDS
================================

A library maintains book information using NamedTuple.

Fields:
book_id, title, author, price

Requirements:

1. Read N book records from the user and store them in a list of NamedTuples.
2. Display all book details.
3. Find and display the most expensive book.
4. Search books by author name.
5. Calculate and display the average price of all books.

---

Test Case:

Input:
Enter number of books: 4

B101 Python Basics John 450
B102 Java Programming James 550
B103 Data Science John 700
B104 SQL Guide Smith 300

Enter Author Name: John

Expected Output:
Most Expensive Book:
B103 Data Science John 700

Average Book Price:
500.0

Books Written By John:
B101 Python Basics John 450
B103 Data Science John 700

'''

from collections import namedtuple
n=int(input("Enter number of books: "))
Books=namedtuple("boook",["b_id","b_title","b_author","b_price"])
book=[]
for i in range(n):
	id=input("Enter book id: ")
	title=input("Enter Book Title: ")
	author=input("Enter Book's Author: ")
	price=int(input("Enter price of a book: "))
	bk=Books(id,title,author,price)
	book.append(bk)
exp=0
sum=0
a_name=input("Enter Author name: ")
for x in book:
	print(f"{x.b_id} {x.b_title} {x.b_author} {x.b_price}")
	if x.b_price>exp:
		exp=x.b_price
	sum+=x.b_price
print("Most Expensive Book: ")
for  x in book:
	if exp==x.b_price:
		print(f"{x.b_id} {x.b_title} {x.b_author} {x.b_price}")
print(f"Average Book price: {sum/n}")
print(f"Books Written by {a_name}: ")
for x in book:
	if x.b_author==a_name:
		print(f"{x.b_id} {x.b_title} {x.b_author} {x.b_price}")