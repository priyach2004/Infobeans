name = None
number = None
address = None
date = None
time_slot = None
service_name = None
status = None
bill = None
rating = 0
feedback=None
cost = None
is_cost_set = False
is_customer = False
electrician_cost=None
plumber_cost=None
ac_repair_cost=None
cleaner_cost=None
carpenter_cost=None
is_booking_pending = False

while True:
    logout_final = False
    print("Let Us know ! Who you are...")
    print("1. Customer")
    print("2. Service Provider")
    person = int(input("Chooose one from above: "))

    if person==2:
        usernameSet = "service"
        passwordSet = "service@123"

        while True:
            username = input("username = ")
            password = input("password = ")
            if username!=usernameSet or password!=passwordSet:
                print("Incorrect username or password!")
                continue
            else:
                print("Login Succesfully!")
                break
        if not is_cost_set:
            electrician_cost=int(input("Enter Electrician Cost: "))
            plumber_cost=int(input("Enter Plumber Cost: "))
            ac_repair_cost=int(input("Enter AC Repair Cost: "))
            cleaner_cost=int(input("Enter Cleaner Cost: "))
            carpenter_cost=int(input("Enter Carpenter Cost: "))
            is_cost_set = True

        while True:
            print("1. View Booking Requests")
            print("2. Accept Booking")
            print("3. Reject Booking")
            print("4. Change Charges")
            print("5. View Ratings")
            print("6. Logout")
            
            choice = int(input("Please select from above: "))
            
            match choice:
                case 1:
                    if is_customer:
                        print(f"Customer Name = {name}")
                        print(f"Address = {address}")
                        print(f"Date = {date}")
                        print(f"Service = {service_name}")
                        print(f"Status = {status}")
                    else:
                        print("No Bookings")
                    logout=False
                    while True:
                        print("1. Back to Dashboard")               
                        print("2. Logout")
                        cho = int(input("Select any one: "))
                        if cho==1:
                            break
                        elif cho==2:
                            print("Logging out... Returning to main menu.")
                            logout = True
                            break
                        else:
                            print("Invalid choice! Please try again.")
                    if logout:
                        break
                case 2:
                    if is_customer:
                        status = "Accepted"
                        print("Booking Accepted...!")
                    else:
                        print("No Customer for booking")
                    logout=False
                    while True:
                        print("1. Back to Dashboard")               
                        print("2. Logout")
                        cho = int(input("Select any one: "))
                        if cho==1:
                            break
                        elif cho==2:
                            print("Logging out... Returning to main menu.")
                            logout = True
                            break
                        else:
                            print("Invalid choice! Please try again.")
                    if logout:
                        break
                case 3:
                    if is_booking_pending:
                        status = "Rejected"
                        print("Booking Rejected Successful...!")
                    elif not is_customer:
                        print("No Bookings For Rejection")
                    else:
                        print("Already Completed")
                    
                    logout=False
                    while True:
                        print("1. Back to Dashboard")               
                        print("2. Logout")
                        cho = int(input("Select any one: "))
                        if cho==1:
                            break
                        elif cho==2:
                            print("Logging out... Returning to main menu.")
                            logout = True
                            break
                        else:
                            print("Invalid choice! Please try again.")
                    if logout:
                        break
                case 4:
                    electrician_cost=int(input("Enter Electrician Cost: "))
                    plumber_cost=int(input("Enter Plumber Cost: "))
                    ac_repair_cost=int(input("Enter AC Repair Cost: "))
                    cleaner_cost=int(input("Enter Cleaner Cost: "))
                    carpenter_cost=int(input("Enter Carpenter Cost: "))
                    print("Charges Changed Successfully")
                    logout=False
                    while True:
                        print("1. Back to Dashboard")               
                        print("2. Logout")
                        cho = int(input("Select any one: "))
                        if cho==1:
                            break
                        elif cho==2:
                            print("Logging out... Returning to main menu.")
                            logout = True
                            break
                        else:
                            print("Invalid choice! Please try again.")
                    if logout:
                        break
                case 5:
                    print(f"Average Rating = {rating}")
                    print(f"Customer's Feedback = {feedback}")
                    logout=False
                    while True:
                        print("1. Back to Dashboard")               
                        print("2. Logout")
                        cho = int(input("Select any one: "))
                        if cho==1:
                            break
                        elif cho==2:
                            print("Logging out... Returning to main menu.")
                            logout = True
                            break
                        else:
                            print("Invalid choice! Please try again.")
                    if logout:
                        break
                case 6:
                    logout_final = True
                    break
        if logout_final:
            continue
    else:
        usernameSet = "customer"
        passwordSet = "customer@123"
        while True:
            username = input("username = ")
            password = input("password = ")
            if username!=usernameSet and password!=passwordSet:
                print("Incorrect username or password!")
                continue
            else:
                print("Login Succesfully!")
                break
        while True:
            is_booking = False
            print("1. Book Sevice")
            print("2. View my booking")
            print("3. Cancel Booking")
            print("4. Give rating")
            print("5. View Profile")
            print("6. Logout")
            choice = int(input("Choose any of above: "))
            match choice:
                case 1:
                    print("These are the services.")
                    print("1. Electrician")
                    print("2. Plumber")
                    print("3. AC Repair")
                    print("4. Cleaner")
                    print("5. Carpenter")
                    service = int(input("Which type of service do you want: "))
                    
                    print("Provide your details: ")
                    name = input("Name: ")
                    number = int(input("Contact Number: "))
                    address = input("Address: ")
                    date = input("Date: ")
                    time_slot = input("Time Slot: ")

                    match service:
                        case 1:
                            bill = electrician_cost+(electrician_cost*(10/100))
                            gst = electrician_cost*(10/100)
                            service_name = "Electrician"
                        case 2:
                            bill = plumber_cost+(plumber_cost*(10/100))
                            gst = plumber_cost*(10/100)
                            service_name = "Plumber"
                        case 3:
                            bill = ac_repair_cost+(ac_repair_cost*(10/100))
                            gst = ac_repair_cost*(10/100)
                            service_name = "AC Repair"
                        case 4:
                            bill = cleaner_cost+(cleaner_cost*(10/100))
                            gst = cleaner_cost*(10/100)
                            service_name = "Cleaner"
                        case 5:
                            bill = carpenter_cost+(carpenter_cost*(10/100))
                            gst = carpenter_cost*(10/100)
                            service_name = "Carpenter"
                    
                    print(f"Estimated Bill...!")
                    print(f"Bill = {bill}")
                    print(f"GST (5%) = {gst}")
                    print(f"Total amount to be paid = {gst+bill}")

                    booking = input("Confirm Booking(yes/no): ")
                    if booking.lower()=="yes":
                        is_customer = True
                        print("Booking Successful")
                        status = "Pending"
                        logout=False
                        is_booking = True
                        while True:
                            print("1. Back to Dashboard")               
                            print("2. Logout")
                            cho = int(input("Select any one: "))
                            if cho==1:
                                break
                            elif cho==2:
                                print("Logging out... Returning to main menu.")
                                logout = True
                                break
                            else:
                                print("Invalid choice! Please try again.")
                        if logout:
                            break
                    else:
                        print("Booking Cancelled Successfully")
                        status = "Cancelled"
                        logout=False
                        while True:
                            print("1. Back to Dashboard")               
                            print("2. Logout")
                            cho = int(input("Select any one: "))
                            if cho==1:
                                break
                            elif cho==2:
                                print("Logging out... Returning to main menu.")
                                logout = True
                                break
                            else:
                                print("Invalid choice! Please try again.")
                        if logout:
                            break
                case 2:
                    if is_booking:
                        print(f"Service Name = {service_name}")
                        print(f"Date = {date}")
                        print(f"Time = {time_slot}")
                        print(f"Status = {status}")
                        print()
                        logout=False
                        while True:
                            print("1. Back to Dashboard")               
                            print("2. Logout")
                            cho = int(input("Select any one: "))
                            if cho==1:
                                break
                            elif cho==2:
                                print("Logging out... Returning to main menu.")
                                logout = True
                                break
                            else:
                                print("Invalid choice! Please try again.")
                        if logout:
                            break
                    else:
                        print("No Bookings...")
                case 3:
                    if is_booking:
                        if status=="Pending":
                            status="Cancelled"
                            print("Cacelled Successfully")
                            cost = 0
                        elif status=="Completed":
                            print("Cannot cance")
                        print()
                        logout=False
                        while True:
                            print("1. Back to Dashboard")               
                            print("2. Logout")
                            cho = int(input("Select any one: "))
                            if cho==1:
                                break
                            elif cho==2:
                                print("Logging out... Returning to main menu.")
                                logout = True
                                break
                            else:
                                print("Invalid choice! Please try again.")
                        if logout:
                            break
                    else:
                        print("No Bookings to cancel...")
                
                case 4:
                    if status=="Completed":
                        rating = int(input("Give rating(1-5): "))
                        feedback = input("Write Feedback: ")
                        print("(❁´◡`❁)--Thank You -- (❁´◡`❁)\nYou rating and feedback have been recorded successfully.\nWe hope to serve you again.")
                        print()
                        logout=False
                        while True:
                            print("1. Back to Dashboard")               
                            print("2. Logout")
                            cho = int(input("Select any one: "))
                            if cho==1:
                                break
                            elif cho==2:
                                print("Logging out... Returning to main menu.")
                                logout = True
                                break
                            else:
                                print("Invalid choice! Please try again.")
                        if logout:
                            break
                    else:
                        print("Give Rating After service is completed")
                case 5:
                    print(f"Name = {name}")
                    print(f"Contact Number = {number}")
                    print(f"Address = {address}")
                    print()
                    logout=False
                    while True:
                        print("1. Back to Dashboard")               
                        print("2. Logout")
                        cho = int(input("Select any one: "))
                        if cho==1:
                            break
                        elif cho==2:
                            print("Logging out... Returning to main menu.")
                            logout = True
                            break
                        else:
                            print("Invalid choice! Please try again.")
                    if logout:
                        break
                case 6:
                    logout_final = True
                    break
        if logout_final:
            continue