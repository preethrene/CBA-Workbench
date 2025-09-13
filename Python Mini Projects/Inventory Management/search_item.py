import csv
from utils import FILE_NAME

def search_item():
    keyword = input("Enter Item Name to Search: ").lower()
    found = False
    with open(FILE_NAME, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if keyword in row['ItemName'].lower():
                print(f"ID: {row['ItemID']} | Name: {row['ItemName']} | Qty: {row['Quantity']} | Price: {row['Price']} | Supplier: {row['Supplier']}")
                found = True
    if not found:
        print("\n No matching items found.\n")

