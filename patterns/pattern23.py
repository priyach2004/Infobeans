'''

a
bc
d f
g  j
klmno

'''

n=int(input("Enter number: "))
i=1
ch = 97
while i<=n:
    j=1
    while j<=i:
        if j==1 or j==i or i==n:
            print(chr(ch),end=" ")
        else:
            print(" ",end=" ")
        ch += 1
        j+=1
    i+=1
    print()