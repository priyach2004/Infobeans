'''

   *
  *_*
 *_*_*
*_*_*_*
 *_*_*
  *_*
   *
   
'''

n=int(input("Enter number: "))
i=1
while i<=n:
    j=1
    while j<=n-i:
        print(" ",end=" ")
        j+=1
    j=1
    while j<=2*i-1:
        if j%2==1:
            print("*",end=" ")
        else:
            print("_",end=" ")
        j+=1
    i+=1
    print()
i=n-1
while i>=1:
    j=1
    while j<=n-i:
        print(" ",end=" ")
        j+=1
    j=1
    while j<=2*i-1:
        if j%2==1:
            print("*",end=" ")
        else:
            print("_",end=" ")
        j+=1
    i-=1
    print()