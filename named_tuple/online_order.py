'''

=====================================================================
QUESTION 4: ONLINE SHOPPING ORDERS
==================================

An online shopping company stores customer orders using NamedTuple.

Fields:
order_id, customer_name, product_name, amount

Requirements:

1. Read N order records from the user and store them in a list of NamedTuples.
2. Display all order details.
3. Find and display the order having the highest amount.
4. Calculate and display total sales.
5. Count the number of orders whose amount is greater than ₹10,000.

---

Test Case:

Input:
Enter number of orders: 5

O101 Rahul Laptop 55000
O102 Priya Mouse 800
O103 Amit Mobile 25000
O104 Neha Keyboard 1500
O105 Rakesh TV 45000

Expected Output:
Highest Value Order:
O101 Rahul Laptop 55000

Total Sales:
127300

Orders Above ₹10,000:
3

'''

from collections import namedtuple
n=int(input("Enter number of orders: "))
orders=namedtuple("Orders",["order_id", "customer_name", "product_name", "product_amount"])
ord=[]
for i in range(n):
	print("Enter details: ")
	o_id=input("Enter order id: ")
	c_name=input("Enter Customer name: ")
	p_name=input("Enter Product name: ")
	p_amount=int(input("Enter Product amount: "))
	ordr=orders(o_id,c_name,p_name,p_amount)
	ord.append(ordr)
highest_amt=0
sum=0
count=0
for x in ord:
	print(f"{x.order_id} {x.customer_name} {x.product_name} {x.product_amount}")
	if highest_amt<x.product_amount:
		highest_amt=x.product_amount
	if x.product_amount>=10000:
		count+=1
	sum+=x.product_amount
print("Highest value order: ")
for x in ord:
	if x.product_amount==highest_amt:
		print(f"{x.order_id} {x.customer_name} {x.product_name} {x.product_amount}")
		break
print("Total sales: ",sum)
print("Orders Above 10,000: ",count)