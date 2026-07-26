'''

    1
   1 2
  1 2 3
 1 2 3 4
1 2 3 4 5

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
            print(j,end="")
        else:
            print(" ",end="")
        j+=1
    i+=1
    print()