import csv
from utils import FILE_NAME

def view_inventory():
    with open(FILE_NAME, mode="r") as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        if not rows:
            print("\n No inventory records found.\n")
            return
        print("\n Inventory Stock Report:")
        print("-" * 70)
        for row in rows:
            print(f"ID: {row['ItemID']} | Name: {row['ItemName']} | Qty: {row['Quantity']} | Price: {row['Price']} | Supplier: {row['Supplier']}")
        print("-" * 70)
