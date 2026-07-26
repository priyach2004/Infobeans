'''

    X
   X X
  X _ X
 X _ _ X
X X X X X

'''

n=int(input("Enter a number: "))
i=1
while i<=n:
    j=1
    while j<=n-i:
        print(" ",end="")
        j+=1
    j=1
    while j<=2*i-1:
        if j%2==1:
            if j==1 or j==(2*i-1) or i==n:
                print("X",end="")
            else:
                print("_",end="")
        else:
            print(" ",end="")
        j+=1
    i+=1
    print()