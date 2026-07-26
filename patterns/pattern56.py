'''

11111
 2222
  333
   44
    5
	
'''

n=int(input("Enter number: "))
i=1
while i<=n:
    j=1
    while j<i:
        print(" ",end=" ")
        j+=1
    j=1
    while j<=(n-i+1):
        print(i,end=" ")
        j+=1
    print()
    i+=1