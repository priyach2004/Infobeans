'''

1
12
123
1234
123
12
1

'''

n=int(input("Enter number: "))
i=1
while i<=n:
    j=1
    while j<=i:
        print(j,end=" ")
        j+=1
    i+=1
    print()
i=n-1
while i>=1:
    j=1
    while j<=i:
        print(j,end=" ")
        j+=1
    i-=1
    print()    