'''
4. Electricity Bill Management System

You are developing an Electricity Bill Management System for a power distribution company. The system helps calculate electricity bills for customers based on their unit consumption.

Sometimes, the operator may try to calculate the bill or apply surcharge before entering the number of units consumed. Your system must handle such situations properly.

👉 Important Condition:
If units are not entered, the system should display:
"Please enter units consumed first"
and should not perform further calculations.

The system should be menu-driven and must continue running until the user selects Exit. All operations should be handled using match-case.

Menu Options:
1 → Enter Units Consumed
2 → Calculate Bill Amount

* First 100 units → ₹5 per unit
* Next 100 units → ₹7 per unit
* Above 200 units → ₹10 per unit
  3 → Apply Surcharge
* If bill > 2000 → 10% surcharge
* Otherwise → 5% surcharge
  4 → Display Final Bill
  5 → Exit

---

Sample Run 1:
Input:
Enter your choice: 2

Output:
Please enter units consumed first

---

Sample Run 2:
Input:
Enter your choice: 1
Enter units consumed: 250

Output:
Units recorded successfully

---

Sample Run 3:
Input:
Enter your choice: 2

Output:
Bill Amount: 1700

(Explanation: 100×5 = 500, 100×7 = 700, 50×10 = 500 → Total = 1700)

---

Sample Run 4:
Input:
Enter your choice: 3

Output:
Surcharge: 85

---

Sample Run 5:
Input:
Enter your choice: 4

Output:
----- Final Bill -----
Units: 250
Bill Amount: 1700
Surcharge: 85
Total Payable: 1785

---

Sample Run 6 (Invalid Choice):
Input:
Enter your choice: 9

Output:
Invalid choice. Please try again.

---

Sample Run 7 (Exit):
Input:
Enter your choice: 5

Output:
Exiting system... Thank you!

---
'''

isUnit = False
while True:
    print("1. Enter Units Consumed")
    print("2. Calculate Bill Amount")
    print("3. Apply Surcharge")
    print("4. Display Final Bill")
    print("5. Exit")
    choice = int(input("Enter a choice: "))
    match choice:
        case 1:
            n = int(input("Enter Units Consumed: "))
            print("Units recorded successfully")
            isUnit = True
        case 2:
            if not isUnit:
                print("Please enter units consumed first")
            else:
                amt = 0 
                if n <= 100:
                    amt = n * 5
                elif n <= 200:
                    unit = n - 100
                    amt = 500 + (unit * 7)
                else:
                    amt = 500 + 700 + ((n - 200)*10)
                print(f"Bill Amount = {amt}")
        case 3:
            if not isUnit:
                print("Please enter units consumed first")
            else:
                amt = 0 
                if n <= 100:
                    amt = n * 5
                elif n <= 200:
                    unit = n - 100
                    amt = 500 + (unit * 7)
                else:
                    amt = 500 + 700 + ((n - 200)*10)
                surcharge = 0
                if amt > 2000:
                    surcharge = amt * (10/1000)
                else:
                    surcharge = amt * (5/100)
                print(f"Surcharge = {surcharge}")
        case 4:
            if not isUnit:
                print("Please enter units consumed first")
                continue
            else:
                amt = 0 
                if n <= 100:
                    amt = n * 5
                elif n <= 200:
                    unit = n - 100
                    amt = 500 + (unit * 7)
                else:
                    amt = 500 + 700 + ((n - 200)*10)
                surcharge = 0
                if amt > 2000:
                    surcharge = amt * (10/1000)
                else:
                    surcharge = amt * (5/100)
                print("-----Final bill-----")
                print(f"Units: {n}")
                print(f"Bill Amount: {amt}")
                print(f"Surcharge: {surcharge}")
                print(f"Total Payable: {amt + surcharge}")
        case 5:
            print("Exiting System... Thank you")
            break
        case _:
            print("Invalid choice. Please try again")