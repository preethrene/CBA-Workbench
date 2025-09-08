# Prime Checker

n = int(input("Number: "))
print("Prime" if all(n%i for i in range(2, n)) and n>1 else "Not Prime")
