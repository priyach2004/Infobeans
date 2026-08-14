'''

7.
Factory Production – Factorial Expansion List

Problem Statement

A factory produces items where production capacity is defined using factorial growth.

Given a list of numbers, replace each number with its factorial value.

Then perform analysis on the resulting list.

Tasks:

Convert each element to factorial
Find sum of all factorial values
Find maximum factorial value
Count how many factorial values are even

Input:
A list of integers

Example 1

Input:
[3, 4, 5]

Processing:
3! = 6
4! = 24
5! = 120

Output:
[6, 24, 120]
Sum = 150
Max = 120
Even Count = 3

'''

arr=list(map(int,input("Enter Elements: ").split()))
factorial=[]
sum=0
max=-1
even_count=0
for i in arr:
    fact=1
    for i in range(1,i+1):
        fact=i*fact
    factorial.append(fact)
    sum+=fact
    if fact%2==0:
        even_count+=1
    if max<fact:
        max=fact
print("Factorial: ",factorial)
print("Sum: ",sum)
print("Max: ",max)
print("Even Count: ",even_count)