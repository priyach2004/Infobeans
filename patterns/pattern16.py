'''

a
bc
def
ghij
klmno

'''

n=int(input("Enter number: "))
i=1
k=97
while i<=n:
    j=1
    while j<=i:
        print(chr(k),end=" ")
        j+=1
        k+=1
    i+=1
    print()