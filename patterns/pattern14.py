'''

1
2 3
4 5 7
8 9 10 11

'''

n=int(input("Enter number: "))
i=1
k=1
while i<=n:
    j=1
    while j<=i:
        print(k,end=" ")
        j+=1
        k+=1
    i+=1
    print()