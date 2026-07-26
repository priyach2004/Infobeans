'''

A
BB
C C
D  D
EEEEE

'''

n=int(input("Enter number: "))
i=1
while i<=n:
    j=1
    ch=65
    while j<=i:
        if j==1 or j==i or i==n:
            print(chr(ch),end=" ")
        else:
            print(" ",end=" ")
        ch += 1
        j+=1
    i+=1
    print()