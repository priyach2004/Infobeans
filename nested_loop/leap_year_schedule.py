'''
9. Leap Year Event Scheduler – Multi-Year Analysis System

A city event management system schedules special festivals only in leap years.

To plan future events, the system analyzes multiple years instead of just one.

Write a program to:

- Read start year and end year from user
- For every year in the range, check whether it is a Leap Year or Not 
- Apply rules:
    - Divisible by 4 → Leap Year candidate  
    - Divisible by 100 → Not Leap Year  
    - Divisible by 400 → Leap Year  

- If leap year → print year with "Event Scheduled"
- Else → print year with "No Event"

- After checking all years:
    - Count total leap years
    - Print total events scheduled

Input:
2000
2005

Output:
2000 → Event Scheduled
2001 → No Event
2002 → No Event
2003 → No Event
2004 → Event Scheduled
2005 → No Event

Total Leap Years = 2
Total Events Scheduled = 2
'''

n1 = int(input("Enter starting number: "))
n2 = int(input("Enter ending number: "))
leap_year = 0
for i in range(n1, n2+1):
    if (i % 400 == 0) or (i % 4 == 0 and i % 100 != 0):
        print(f"{i} → Event Scheduled")
        leap_year += 1
    else:
        print(f"{i} → No Event")
print(f"Total Leap years = {leap_year}")
print(f"Total Events Scheduled = {leap_year}")
