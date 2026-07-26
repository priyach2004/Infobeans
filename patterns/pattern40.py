'''

*
**
****
*******
***********

'''

n=int(input("Enter number: "))
i=1
a=1
b=1
while i<=n:
    j=1
    while j<=b:
        print("*",end=" ")
        j+=1
    b+=a
    a+=1
    i+=1
    print()