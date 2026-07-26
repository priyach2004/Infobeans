'''

ABCDE
 A__D
  A_C
   AB
    A
	
'''

n=int(input("Enter a number: "))
i=n
while i>=1:
    j=1
    while j<=n-i:
        print(" ",end=" ")
        j+=1
    
    j=1
    ch=65
    while j<=i:
        if j==1 or j==i or i==n:
            print(chr(ch),end=" ")
        else:
            print("_",end=" ")
        j+=1
        ch+=1
    print()
    i-=1