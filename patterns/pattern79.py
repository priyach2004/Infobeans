'''

1
12
1 3
1  4
1 3
12
1

'''

n=int(input("Enter number: "))
i=1
while i<=n:
    j=1
    while j<=i:
        if j==1 or j==i:
            print(j,end=" ")
        else:
            print(" ",end=" ")
        j+=1
    i+=1
    print()
i=n-1
while i>=1:
    j=1
    while j<=i:
        if j==1 or j==i:
            print(j,end=" ")
        else:
            print(" ",end=" ")
        j+=1
    i-=1
    print()    