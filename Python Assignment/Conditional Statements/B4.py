# Movie Ticket

time = int(input("Show time (24h): "))
price = 200
print("Price:", price*0.7 if time<17 else price)
