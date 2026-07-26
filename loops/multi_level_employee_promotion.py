'''
9. Multi-Level Employee Promotion System

A company promotes employees based on experience, rating, projects completed, and salary.

If experience is at least 5 years, then check rating. If rating is at least 4, then check projects. If projects are at least 3, then check salary. If salary is up to 50000, promote with 30 percent hike; otherwise 20 percent hike. If projects are less than 3, promote with 10 percent hike. If rating is below 4, no promotion. If experience is less than 5, then check if rating is 5. If yes, fast track promotion; otherwise no promotion.

Input:
Experience = 6
Rating = 4
Projects = 2

Output:
Promotion Status = Promoted with 10% hike
'''

exp = int(input("Enter Experience: "))
rat = int(input("Enter Rating: "))
project = int(input("Enter number of projects: "))
salary=int(input("Enter salary: "))
status=""
if exp>=5:
    if rat>=4:
        if project>=3:
            if salary<=50000:
                status="Promoted with 30% hike"
            else:
                status="Promoted with 20% hike"
        else:
            status = "Promoted with 10% hike"
    else:
        status="No Promotion"
else:
    if rat==5:
        status="Fast Track Promotion"
    else:
        status="No Promotion"
print(f"Promotion Status = {status}")