'''
0
01
012
0123
01234
'''

n=int(input("Enter n: "))
i=1
while i<=n:
    print()
    j=1
    while j<=i:
        print(j-1,end=" ")
        j=j+1
    i=i+1