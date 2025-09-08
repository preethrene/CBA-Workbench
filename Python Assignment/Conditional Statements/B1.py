age = int(input("Age: "))
fare = "Free" if age<5 else "Full" if age<=60 else "Half"
print("Ticket:", fare)
