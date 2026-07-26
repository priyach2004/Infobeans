'''

ABCDE
A  D
A C
AB
A

'''

n=int(input("Enter number: "))
i=n
while i>=1:
    j=1
    ch = 65
    while j<=i:
        if j==1 or i==j or i==n:
            print(chr(ch),end=" ")
        else:
            print(" ",end=" ")
        j+=1
        ch+=1
    i-=1
    print()