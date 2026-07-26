'''
5. Website URL Verification System

A software company is developing an automated website registration
portal. Before saving a website address, the system must verify whether
the URL follows the required company format.

Conditions: - Must start with www 
			- Must end with .com

Input: Enter website: www.amazon.com

Output: Valid Website

'''

s=input("Enter Website: ")
l = len(s)
if s[0]== "w" and s[1]== "w" and s[2]=="w" and s[l-4]=="." and s[l-3] == "c" and s[l-2]=="o" and s[l-1]=="m":
	print("Valid Website")
else:
	print("Invalid website")
    
# if s[:4] == "www." and s[-4:] == ".com":