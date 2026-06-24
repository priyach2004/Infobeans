'''
14.Floor Movement System (Elevator)
An elevator system takes the current floor and destination floor as input.

If current floor < destination → move upward and display floors
If current floor > destination → move downward and display floors
If both are same → display "Already on the same floor"

Write a program using if-elif-else and loops to simulate elevator movement.

Input: 1, 5
Output: 1 → 2 → 3 → 4 → 5

Input: 7, 3
Output: 7 → 6 → 5 → 4 → 3

Input: 4, 4
Output: Already on the same floor
'''

curr, dest = map(int, input("Enter two numbers: ").split(","))
if curr < dest:
    i=curr
    while i<dest:
        print(i, end=" → ")
        i += 1
    print(dest)
elif curr > dest:
    i=curr
    while i>dest:
        print(i, end=" → ")
        i -= 1
    print(dest)
else:
    print("Already on the same floor")

'''
curr, dest = map(int, input("Enter two numbers: ").split(","))
if curr < dest:
    for i in range(curr, dest):
        print(i, end=" → ")
    print(dest)
elif curr > dest:
    for i in range(curr, dest, -1):
        print(i, end=" → ")
    print(dest)
else:
    print("Already on the same floor")
'''