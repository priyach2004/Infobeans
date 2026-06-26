'''
5. Count Factors of Number
A mathematics learning app gives practice questions where students must know how many factors a number has. The app should automatically count the total factors of the entered number.
Write a program to count total factors of a number using loops.

Input:
12

Output:
Factors Count = 6
'''

n = int(input("Enter a number: "))
count=0
for i in range(1,n+1):
    if n%i==0:
        count += 1
    i+=1
print(f"Factors Count = {count}")

'''
n = int(input("Enter a number: "))
i=1
count=0
while i<=n:
    if n%i==0:
        count += 1
    i+=1
print(f"Factors Count = {count}")
'''