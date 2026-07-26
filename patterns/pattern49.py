'''

    1
   10
  101
 1010
10101

'''

n=int(input("Enter number: "))
i=1
while i<=n:
	j=1
	while j<=n-i:
		print(" ",end=" ")
		j+=1
	j=1
	while j<=i:
		if j%2==0:
			print("0",end=" ")
		else:
			print("1",end=" ")
		j+=1
	i+=1
	print()