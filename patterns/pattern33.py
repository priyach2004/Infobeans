'''


ABCDE
ABCD
ABC
AB
A

'''

n=int(input("Enter number: "))
i=n
while i>=1:
	j=1
	ch=65
	while j<=i:
		print(chr(ch),end=" ")
		j+=1
		ch+=1
	i-=1
	print()