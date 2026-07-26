'''

*
 *
  *
   *
    *

'''

n=int(input("Enter number: "))
i=1
while i<=n:
    j=1
    while j<=i:
        if i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        j+=1
    i+=1
    print()