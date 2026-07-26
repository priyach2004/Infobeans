'''
Program to find out all the leap years between two entered years.
'''

n1 = int(input("Enter starting number: "))
n2 = int(input("Enter ending number: "))
leap_year = 0
for i in range(n1, n2+1):
    if (i % 400 == 0) or (i % 4 == 0 and i % 100 != 0):
        print(i,end=" ")