'''

123456789
 1+++++7
  1+++5
   1+3
    1
	
'''

n=int(input("Enter a number: "))
i=n
while i>=1:
	j=1
	while j<=n-i:
		print(" ",end="")
		j+=1
	j=1
	while j<=2*i-1:
		if j==1 or j==2*i-1 or i==n:
			print(j,end="")
		else:
			print("+",end="")
		j+=1
	i-=1
	print()