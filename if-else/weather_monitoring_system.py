'''
6. Weather Monitoring System
   A system checks weather conditions:

* If temperature ≥ 30 → Hot day
* If humidity ≥ 70 → High humidity alert

Input:
Enter temperature: 32
Enter humidity: 75

Output:
Hot day
High humidity alert
'''

temp = int(input("Enter Temperature: "))
humidity = int(input("Enter Humidity: "))
if temp>=30:
        print("Hot day")
if humidity>=70:       
    print("High humidity alert")