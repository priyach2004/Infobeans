'''

5
54
543
5432
54321

'''

n=int(input("Enter number: "))
i=1
while i<=n:
    j=5
    while j>n-i:
        print(j,end=" ")
        j-=1
    i+=1
    print()