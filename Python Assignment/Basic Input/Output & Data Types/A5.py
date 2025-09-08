amt = float(input("Enter amount: "))
disc = 0.2 if amt>5000 else 0.1
print("Final:", amt - amt*disc)
