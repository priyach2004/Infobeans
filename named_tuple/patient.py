'''

=====================================================================
QUESTION 3: HOSPITAL PATIENT TRACKER
====================================

A hospital stores patient records for daily monitoring.

Fields:
patient_id, patient_name, age, disease

Requirements:

1. Read N patient records from the user and store them in a list of NamedTuples.
2. Display all patient details.
3. Display patients whose age is above 60 years.
4. Search for a patient using Patient ID.
5. Count the number of patients suffering from a particular disease.

---

Test Case:

Input:
Enter number of patients: 4

P101 Rajesh 65 Diabetes
P102 Suman 45 Fever
P103 Mohan 70 Diabetes
P104 Rita 35 Cold

Enter Patient ID: P103
Enter Disease: Diabetes

Expected Output:
Patient Found:
P103 Mohan 70 Diabetes

Patients Above 60:
P101 Rajesh 65 Diabetes
P103 Mohan 70 Diabetes

Patients with Diabetes:
2

'''

from collections import namedtuple
n=int(input("Enter number of patients: "))
patient=namedtuple("Patients",["p_id","p_name","p_age","p_disease"])
pat=[]
for i in range(n):
	print("Enter details: ")
	id=input("Enter Patien id: ")
	name=input("Enter Patient name: ")
	age=int(input("Enter Patient's Age: "))
	disease=input("Enter patient disease: ")
	patnt=patient(id,name,age,disease)
	pat.append(patnt)
p_id_input=input("Enter a patient id: ")
p_disease_input=input("Enter a disease name: ")
count=0
for x in pat:
	print(f"{x.p_id} {x.p_name} {x.p_age} {x.p_disease}")
	if p_disease_input==x.p_disease:
		count+=1
print("Patients details whose age is above 60: ")
for x in pat:
	if x.p_age>=60:
		print(f"{x.p_id} {x.p_name} {x.p_age} {x.p_disease}")
print("Patient Found: ")
for x in pat:
	if p_id_input==x.p_id:
		print(f"{x.p_id} {x.p_name} {x.p_age} {x.p_disease}")
		break
print(f"Patient with {p_disease_input}: {count}")