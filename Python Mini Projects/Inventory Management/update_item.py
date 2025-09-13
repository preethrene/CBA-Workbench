import csv
from utils import FILE_NAME

def update_item():
    itemid = input("Enter Item ID to Update: ")
    updated = False
    rows = []

    with open(FILE_NAME, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['ItemID'] == itemid:
                print(f"\nCurrent Item: {row}")
                choice = input("Update (1) Quantity or (2) Price? Enter choice: ")
                if choice == '1':
                    row['Quantity'] = input("Enter New Quantity: ")
                elif choice == '2':
                    row['Price'] = input("Enter New Price: ")
                else:
                    print("\n⚠️ Invalid choice. Skipping update.\n")
                updated = True
            rows.append(row)

    if updated:
        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["ItemID", "ItemName", "Quantity", "Price", "Supplier"])
            writer.writeheader()
            writer.writerows(rows)
        print("\n✅ Item updated successfully!\n")
    else:
        print("\n❌ Item not found.\n")
