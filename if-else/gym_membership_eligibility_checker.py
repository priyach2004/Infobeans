'''
4. Gym Membership Eligibility Checker
   A gym checks multiple conditions:

* If age ≥ 18 → Allowed for gym
* If BMI > 25 → Suggest weight loss program

Input:
Enter age: 25
Enter BMI: 27

Output:
Gym access granted
Enroll in weight loss program
'''

age = int(input("Enter age: "))
bmi = int(input("Enter bmi value: "))
if age>=18:
        print("Gym access granted")
if bmi>27:       
    print("Enroll in weight loss program")