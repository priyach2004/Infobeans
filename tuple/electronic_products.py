'''
6.

NOTE: using tuple only
An electronics store wants to maintain product information. Since product details should not be modified accidentally,
 each product record is stored as a tuple.

Tuple Format:

(product_id, product_name, price)

Requirements:

Read N product details from the user and store them as tuples in a list.
Display all product details.
Find and display the costliest product.
Find and display the cheapest product.
Calculate and display the average price of all products.
Display all products whose price is greater than ₹50,000.

Test Case:

Input:

Enter number of products: 4

P101 Laptop 65000
P102 Mobile 25000
P103 Television 80000
P104 Tablet 30000

Expected Output:

All Products:
('P101', 'Laptop', 65000)
('P102', 'Mobile', 25000)
('P103', 'Television', 80000)
('P104', 'Tablet', 30000)

Costliest Product:
('P103', 'Television', 80000)

Cheapest Product:
('P102', 'Mobile', 25000)

Average Price:
50000.0

Products Above ₹50,000:
('P101', 'Laptop', 65000)
('P103', 'Television', 80000)
'''

n=int(input("Enter number of products: "))
product=[]
for i in range(n):
	id = input("Enter ID of a Product: ")
	name=input("Enter name of a Product: ")
	price=int(input("Enter price: "))
	t=(id,name,price)
	product.append(t)

print(product)

costliest=product[0][2]
cheapest=product[0][2]
sum=0
for i in product:
    if i[2]<costliest:
        costliest=i[2]
    if cheapest>i[2]:
        cheapest=i[2]
    sum+=i[2]
for x in product:
    if x[2]==costliest:
        print("Costliest Product: ")
        print(x)
    if x[2]==cheapest:
        print("Cheapesr product: ")
        print(x)
print("Average Price: ",(sum/n))
print("Products Above ₹50,000:")
for i in product:
    if i[2]>=50000:
        print(x)