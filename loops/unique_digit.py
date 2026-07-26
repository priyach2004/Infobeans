'''
4.Unique Digit Security Scanner

A smart locker accepts only numbers whose all digits are unique.

Write a program using for-else loop to:

- Check every digit
- If any repeated digit found reject
- Else accept

Input:
57294

Output:
Valid Unique Code
'''

n = int(input("Enter a number: "))
temp = n
x=0
if len(str(n)) == 1:
    print("Valid Unique Code")
else:
    for i in range(len(str(temp))):
        d = n % 10
        n = n // 10
        while n > 0:
            if d != (n % 10):
                n = n // 10
                continue
            else:
                print("Rejected")
                x=1
                break
            n=n//10
        if x==1:
            break
    else:
        print("Valid Unique Code")