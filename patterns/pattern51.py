'''

5 5 5 5 5
  4 4 4 4
    3 3 3
      2 2
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
        print(i,end=" ")
        j+=1
    print()
    i-=1