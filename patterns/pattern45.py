'''

    5
   44
  333
 2222
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
        print(i,end=" ")
        j+=1
    i-=1
    print()