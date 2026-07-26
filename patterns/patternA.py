'''

     *
    **
   ***
  ****
 *****
******

'''

n = int(input("Enter n: "))
i=1
while i<=n:
    print()
    j = 1
    while  j<=n-i:
        print(" ",end=" ")
        j = j+1
    j=1
    while j<=i:
        print("*",end=" ")
        j=j+1
    i=i+1