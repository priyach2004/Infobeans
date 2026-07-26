'''
    1
   10
  101
 1010
10101

'''

n=int(input("Enter n: "))
i=1
while i<=n:
	print()
	j=1
	while j<=n-i:
		print(" ",end=" ")
		j=j+1
	j = 1
	while j<=i:
		if j%2!=0:
			print("1",end=" ")
		else:
			print("0",end=" ")
		j=j+1
	i=i+1