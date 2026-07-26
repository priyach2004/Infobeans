'''

*****
*  *
* *
**
*

'''

n=int(input("Enter number: "))
i=n
while i>=1:
    j=1
    while j<=i:
        if j==1 or i==j or i==n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        j+=1
    i-=1
    print()