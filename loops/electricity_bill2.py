'''
10.
Electricity Bill Processing System (Multi-House)

An electricity board processes bills for multiple houses in a society.

Write a program to:

- Read number of houses n
- For each house:
    - Read units consumed
    - Calculate bill using slab rates:

        First 100 units      → ₹5 per unit  
        Next 100 units      → ₹7 per unit  
        Above 200 units     → ₹10 per unit  

    - Apply conditions:
        - If bill > ₹2000 → add 10% surcharge  
        - If units < 50 → give ₹100 subsidy  

    - Print bill for each house

- After processing all houses:
    - Print total bill collected
    - Print highest bill

---

Input:
3
120
250
40

Output:
House 1 Bill = 640
House 2 Bill = 1700
House 3 Bill = 100

Total Collection = 2440
Highest Bill = 1700
'''

n = int(input("Enter a number: "))
total = 0
highest_bill = 0
amt = 0
i = 1

while n >= 1:
    unit = int(input("Enter units consumed: "))
    if unit <= 100:
        amt = 5 * unit
        if unit<50:
            amt=amt-100
    elif unit <= 200:
        rem = unit - 100
        amt = (rem * 7) + 500
    else:
        rem = unit - 200
        amt = (rem * 10) + 500 + 700
    if amt>2000:
        amt += (amt*(10/100))
    total += amt
    if highest_bill < amt:
        highest_bill = amt

    print(f"House {i} Bill = {amt}")
    n -= 1
    i += 1

print(f"Total Collection = {total}")
print(f"Highest Bill = {highest_bill}")
