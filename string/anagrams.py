'''

6. Product Code Verification System

An e-commerce company wants to verify whether two product codes are rearranged versions of each other.

Conditions:
- Ignore spaces
- Ignore case sensitivity

Input:
Enter first product code: Dormitory
Enter second product code: Dirty Room

Output:
Both Product Codes are Matching

'''

code1=input("Enter first product code: ").lower()
code2=input("Enter second product code: ").lower()
x=1
i=0
while i<len(code1):
    ch=code1[i]
    c1=0
    c2=0
    j=0
    while j<len(code1):
        if code1[j]==ch:
            c1=c1+1
        j=j+1
    j=0
    while j<len(code2):
        if code2[j]==ch:
            c2=c2+1
        j=j+1
    if c1 != c2:
        x=0
        break
    i=i+1
if x==1:
    print("Anagrams")
else:
    print("Not Anagrams")