'''

A
BCD
EFGHI
JKLMNOP

'''

n=int(input("Enter number: "))
i=1
ch = 65
while i<=n:
    j=1
    while j<=2*i-1:
        print(chr(ch),end=" ")
        j+=1
        ch+=1
    i+=1
    print()