'''
9. Bike Service Kilometer Checker

A bike needs service every 3000 km.

Write a program to:

- Read travelled kilometers
- Print every service checkpoint till entered km

Input:
10000

Output:
3000 6000 9000
'''

n=int(input("Enter a number: "))
if n<3000:
    print("No service needed")
else:    
    num=3000
    for i in range(1,(n//3000)+1):
        print(num*i,end=" ")
	