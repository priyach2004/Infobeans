'''

    A
   A B
  A B C
 A B C D
A B C D E

'''

n=int(input("Enter a number: "))
i=1
while i<=n:
    j=1
    while j<=n-i:
        print(" ",end="")
        j+=1
    j=1
    ch=65
    while j<=2*i-1:
        if j%2==1:
            print(chr(ch),end="")
            ch+=1
        else:
            print(" ",end="")
        j+=1
    i+=1
    print()