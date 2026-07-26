'''

A B C D E
 A B C D
  A B C
   A B
    A
	
'''

n=int(input("Enter a number: "))
i=n
while i>=1:
	j=1
	ch=65
	while j<=n-i:
		print(" ",end="")
		j+=1
	j=1
	while j<=i:
		print(chr(ch),end=" ")
		ch+=1
		j+=1
	i-=1
	print()