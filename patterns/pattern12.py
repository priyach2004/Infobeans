'''

a
a b
a b c
a b c d
a b c d e

'''

n=int(input("Enter number: "))
i=1
while i<=n:
    ch=97
    j=1
    while j<=i:
        print(chr(ch),end=" ")
        ch+=1
        j+=1
    i+=1
    print()