# Banking System (5% interest, 12 months)

bal = float(input("Balance: "))
for m in range(1, 13):
    bal *= 1.05
    print(f"Month {m}: {bal:.2f}")
