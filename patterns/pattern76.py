'''

X
XX
XXX
XXXX
XXX
XX
X

'''

n=int(input("Enter number: "))
i=1
while i<=n:
    j=1
    while j<=i:
        print("X",end=" ")
        j+=1
    i+=1
    print()
i=n-1
while i>=1:
    j=1
    while j<=i:
        print("X",end=" ")
        j+=1
    i-=1
    print()    