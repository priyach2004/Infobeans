'''

123456789
 1234567
  12345
   123
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
	while j<=2*i-1:
		print(j,end=" ")
		j+=1
	i-=1
	print()