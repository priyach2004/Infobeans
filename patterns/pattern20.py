'''

1
12
1 3
1  4
12345

'''

n=int(input("Enter number: "))
i=1
while i<=n:
    j=1
    while j<=i:
        if j==1 or j==i or i==n:
            print(j,end=" ")
        else:
            print(" ",end=" ")
        j+=1
    i+=1
    print()