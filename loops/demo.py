'''
n1,n2 = map(int,input("Enter two numbers: ").split(","))
if n1<n2:
	for i in range(n1,n2+1):
		if i%2==0:
			print(i,end = " ")
elif n1>n2:
	for i in range(n1,n2-1,-1):
		if i%2==1:
			print(i,end = " ")
'''

n1,n2 = map(int,input("Enter two numbers: ").split(","))
if n1<n2:
    i=n1
    while i<=n2:
        if i%2==0:
            print(i,end = " ")
        i+=1
elif n1>n2:
    i = n1
    while i>=n2:
        if i%2==1:
            print(i,end = " ")
        i-=1