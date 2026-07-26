'''

2. Mobile Number Digit Counter

A telecom company wants to count how many digits are present in a customer contact number entered with spaces or symbols.

Input:
Enter contact number: +91 98765-43210

Output:
Total digits: 12

'''

number = input("Enter Contact Nummber: ")
length = len(number)
count = 0
i=0
while i<length:
	if number[i] in "1234567890":
		count+=1
	i+=1
print(f"Total Digits: {count}")