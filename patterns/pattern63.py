'''
    A
   ABC
  ABCDE
 ABCDEFG
ABCDEFGHI

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
        print(chr(ch),end="")
        j+=1
        ch+=1
    i+=1
    print()