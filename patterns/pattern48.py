'''

A
AB
A_C
A__D
ABCDE

'''

n=int(input("Enter number: "))
i=n
while i>=1:
    j=1
    while j<=i-1:
        print(" ",end=" ")
        j+=1
    
    j=1
    ch = 65
    while j<=n-i+1:
        if j==1 or j==n-i+1 or i==1:
            print(chr(ch),end=" ")
        else:
            print("*",end=" ")
        j+=1
        ch+=1
    i-=1
    print()