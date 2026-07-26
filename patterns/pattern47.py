'''

    1
   11
  1*1
 1**1
11111

'''

n=int(input("Enter number: "))
i=n
while i>=1:
    j=1
    while j<=i-1:
        print(" ",end=" ")
        j+=1
    
    j=1
    while j<=n-i+1:
        if j==1 or j==n-i+1 or i==1:
            print("1",end=" ")
        else:
            print("*",end=" ")
        j+=1
    i-=1
    print()