'''
2. Next Prime ID Generator

A multinational company auto-generates employee IDs in numeric sequence.
Due to internal policy, only prime numbered IDs are assigned to new premium employees.

The HR manager enters the current last issued ID, and the software must search forward to find the next available prime number ID.

Write a program to find the first prime number after n.

Input:
14

Output:
Next Prime = 17
'''
import  math
n = int(input("Enter a number: "))
if n<=2:
    num=n+1
else:
    num = n+1
    x=0
    while x!=1:
        i=2
        while i<=int(math.sqrt(num)):
            if num%i==0:
                num=num+1
                break
            i = i+1
        else:
            x=1
print(num)