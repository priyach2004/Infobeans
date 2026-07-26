'''

*****
****
***
**
*

'''

n=int(input("Enter number: "))
i=1
while i<=n:
	j=n-i+1
	while j>=1:
		print("*",end=" ")
		j-=1
	i+=1
	print()