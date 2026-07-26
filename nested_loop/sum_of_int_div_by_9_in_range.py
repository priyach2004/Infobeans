'''
program to find out the sum of all integers between 100 and 200 which are divisible ny 9
'''

sum=0
for i in range(100,201):
    if i%9==0:
        sum += i 
print(f"Sum = {sum}")