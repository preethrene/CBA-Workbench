import csv
from utils import FILE_NAME

def add_item():
    itemid = input("Enter Item ID: ")
    name = input("Enter Item Name: ")
    quantity = input("Enter Quantity: ")
    price = input("Enter Price: ")
    supplier = input("Enter Supplier: ")

    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([itemid, name, quantity, price, supplier])

    print("\n✅ Item added successfully!\n")
