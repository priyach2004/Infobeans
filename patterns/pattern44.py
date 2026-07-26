'''

    1
   22
  333
 4444
55555

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
		print(i,end=" ")
		j+=1
	i+=1
	print()