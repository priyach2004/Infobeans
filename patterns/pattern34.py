'''

EEEEE
DDDD
CCC
BB
A

'''

n=int(input("Enter number: "))
i=n
ch = 65+n-1
while i>=1:
	j=1
	while j<=i:
		print(chr(ch),end=" ")
		j+=1
	i-=1
	ch-=1
	print()