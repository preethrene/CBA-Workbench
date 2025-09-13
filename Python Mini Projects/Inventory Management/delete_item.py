import csv
from utils import FILE_NAME

def delete_item():
    itemid = input("Enter Item ID to Delete: ")
    deleted = False
    rows = []

    with open(FILE_NAME, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['ItemID'] == itemid:
                deleted = True
            else:
                rows.append(row)

    if deleted:
        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["ItemID", "ItemName", "Quantity", "Price", "Supplier"])
            writer.writeheader()
            writer.writerows(rows)
        print("\n🗑️ Item deleted successfully!\n")
    else:
        print("\n❌ Item not found.\n")
