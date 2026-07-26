'''

    1
   212
  32123
 4321234
543212345

'''

n=int(input("Enter number: "))
i=1
while i<=n:
    j=1
    while j<=n-i:
        print(" ",end=" ")
        j+=1
    j=i
    while j>=1:
        print(j,end=" ")
        j-=1
    j=2
    while j<=i:
        print(j,end=" ")
        j+=1
    i+=1
    print()