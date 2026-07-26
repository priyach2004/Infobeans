'''

55555
 4__4
  3_3
   22
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
            print(i,end=" ")
        else:
            print("_",end=" ")
        j+=1
    print()
    i-=1