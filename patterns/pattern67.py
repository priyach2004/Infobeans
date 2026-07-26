'''

    A
   B B
  C   C
 D     D
EEEEEEEEE

'''

n=int(input("Enter a number: "))
i=1
ch = 65
while i<=n:
    j=1
    while j<=n-i:
        print(" ",end="")
        j+=1
    j=1
    while j<=2*i-1:
        if j==1 or j==(2*i-1) or i==n:
            print(chr(ch),end="")
        else:
            print(" ",end="")
        j+=1
    i+=1
    print()
    ch+=1