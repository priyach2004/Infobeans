'''
654321
 65432
  6543
   654
    65
	 6
'''

n=int(input("Enter n: "))
i=1
while i<=n:
    j=n
    while j>=i:
        print(j,end = " ")
        j=j-1
    print()
    j=1
    while j<=i:
        print(" ",end=" ")
        j=j+1
    i=i+1