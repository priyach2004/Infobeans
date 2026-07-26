n = input("Number: ")
ls=len(n)
num = int(n)
ns = len(str(n))
if ls==ns:
    if n%(10**l) != 0:
        while n>0:
            if n%10==0:
                break
            n=n//10
        else:
            print("Non Duck Number")
else:
    print("Duck Number")