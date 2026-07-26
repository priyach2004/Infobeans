'''

    1
   123
  12345
 1234567
123456789

'''


n=int(input("Enter a number: "))
i=1
while i<=n:
    j=1
    while j<=n-i:
        print(" ",end="")
        j+=1
    j=1
    while j<=2*i-1:
        print(j,end="")
        j+=1
    i+=1
    print()