'''

A
AB
ABC
ABCD
ABCDE

'''

n=int(input("Enter number: "))
i=1
while i<=n:
    ch=65
    j=1
    while j<=i:
        print(chr(ch),end=" ")
        ch+=1
        j+=1
    i+=1
    print()