'''
1. Product of Odd Numbers up to N

A puzzle game rewards players by multiplying odd numbers up to n.
Write a program using loops to find product of odd numbers.

Input:
5

Output:
15
'''

n = int(input("Enter a number: "))
prod = 1
for i in range(n+1):
    if i%2==1:
        prod *= i
print(prod)