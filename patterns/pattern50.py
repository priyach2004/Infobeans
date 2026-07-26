'''

12345
 1234
  123
   12
    1
	
'''

'''
n=int(input("Enter number: "))
i=1
while i<=n:
    j=1
    while j<=n-i+1:
        print(j,end=" ")
        j+=1
    print()
    j=0
    while j<=i-1:
        print(" ",end=" ")
        j+=1
    i+=1
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
        print(j,end=" ")
        j+=1
    print()
    i-=1