'''
QNo 8:--
SMART TEXT PROCESSING SYSTEM

A software company is developing a Smart Text Processing System for
handling user messages. Different users require different text
transformations. To avoid creating separate applications, the company
wants a menu-driven program where users can select operations according
to their requirements.

The system should continue executing until the user selects Exit.

====================================================== MENU
======================================================

===== Smart Text Processing System =====

1.  Reverse Complete String
2.  Reverse Every Word
3.  Reverse Word Order
4.  Exit

====================================================== Choice 1 :

Conditions: - Reverse the complete string 
			- Ignore extra spaces 
			- Keep special characters (@,#,$,%) in their original positions 
			- Do not use built-in reverse functions

Example: Input: ja@va#py

Output: yp@av#aj

Test Case 1: ab@cd#ef Output: fe@dc#ba

Test Case 2: py@th#on Output: no@ht#yp

Test Case 3: java@proOutput : orpa@vaj

====================================================== Choice 2 :

Conditions: - Reverse every word separately 
			- Words containing digits should not be reversed 
			- Ignore extra spaces between words 
			- First letter of each reversed word should become uppercase

Example: Input: java is easy123 programming

Output: Avaj Si easy123 Gnimmargorp

Test Case 1: python full stack22 developer Output: Nohtyp Lluf stack22
Repoleved

Test Case 2: hello java99 world Output: Olleh java99 Dlrow

====================================================== Choice 3 :

Conditions: - Reverse order of words - Remove duplicate words - Ignore
case while checking duplicates - Keep only first occurrence

Example: Input: Java python Java react Python

Output: React Python Java

Test Case 1: HTML CSS HTML Java CSS Output: Java CSS HTML

Test Case 2: Python React Java Python React Output: Java React Python

====================================================== Choice 4
======================================================

Program Closed Successfully
'''

while True:
	print("===== Smart Text Processing System =====")
	print("1.  Reverse Complete String")
	print("2.  Reverse Every Word")
	print("3.  Reverse Word Order")
	print("4.  Exit")
	choice = int(input("Select any one: "))
	match choice:
		case 1:
			s=input("Input: ") #ja@va#py
			i=0
			j=len(s)-1
			result=""
			while i<len(s) and j>=0:
				if (65<=ord(s[i])<=90 or 97<=ord(s[i])<=122) and (65<=ord(s[j])<=90 or 97<=ord(s[j])<=122):
					result = result+s[j]
					i+=1
					j-=1
				elif not (65<=ord(s[i])<=90 or 97<=ord(s[i])<=122):
					result = result+s[i]
					i+=1
				elif not (65<=ord(s[j])<=90 or 97<=ord(s[j])<=122):
					j-=1
			print(f"Output = {result}")
		case 2:
			s=input("Input: ") #java is easy123 programming
			i=0
			result=""
			while i<len(s):
				j=i
				digit = False
				while j<len(s) and s[j]!=" ":
					if s[j] in "1234567890":
						digit = True
					j+=1
				rev = ""
				if not digit:
					word = s[i:j]
					rev=word[::-1]
					if 97<=ord(rev[0])<=122:
						result = result+chr(ord(rev[0])-32)+rev[1::]+" "
				else:
					result = result+s[i:j]+" "
				i=j+1
			print(f"Output = {result}")
		case 3:
			s=input("Enter string: ") 	#HTML CSS HTML Java CSS Output: Java CSS HTML
			st=s.split()
			res=""
			for ch in st:
				if ch not in res:
					res=res+ch+" "
			res1=""
			r1=res.split()
			for ch in r1:
				res1=ch+" "+res1
			print(f"Output: {res1}")
		case 4:
			print("Program Closed Successfully")
			break