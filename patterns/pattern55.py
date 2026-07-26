'''

ABCDE
 ABCD
  ABC
   AB
    A

'''


n=int(input("Enter a number: "))
i=n
while i>=1:
    j=1
    ch=65
    while j<=n-i:
        print(" ",end=" ")
        j+=1
    
    j=1
    while j<=i:
        print(chr(ch),end=" ")
        j+=1
        ch+=1
    print()
    i-=1