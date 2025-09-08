# Electricity bill 

u = int(input("Units: "))
rate = 5 if u<=100 else 7 if u<=300 else 10
print("Bill:", u*rate)
