'''

12345
 1__4
  1_3
   12
    1
	
'''

n=int(input("Enter a number: "))
i=n
while i>=1:
    j=1
    while j<=n-i:
        print(" ",end=" ")
        j+=1
    
    j=1
    while j<=i:
        if j==1 or j==i or i==n:
            print(j,end=" ")
        else:
            print("_",end=" ")
        j+=1
    print()
    i-=1