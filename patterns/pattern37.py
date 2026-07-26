'''

*****
####
***
##
*

'''

n=int(input("Enter number: "))
i=n
while i>=1:
	j=1
	while j<=i:
		if i%2!=0:
			print("*",end=" ")
		else:
			print("#",end=" ")
		j+=1
	i-=1
	print()