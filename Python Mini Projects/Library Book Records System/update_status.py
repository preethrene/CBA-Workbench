import csv
from utils import FILE_NAME

def update_status():
    bookid = input("Enter Book ID to Update Status: ")
    updated = False
    rows = []

    with open(FILE_NAME, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['BookID'] == bookid:
                print(f"\nCurrent Status: {row['Status']}")
                choice = input("Enter New Status (Available/Borrowed): ")
                if choice.lower() in ["available", "borrowed"]:
                    row['Status'] = choice.capitalize()
                    updated = True
                else:
                    print("\n⚠️ Invalid status entered. Keeping old status.\n")
            rows.append(row)

    if updated:
        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["BookID", "Title", "Author", "Year", "Status"])
            writer.writeheader()
            writer.writerows(rows)
        print("\n✅ Book status updated successfully!\n")
    else:
        print("\n❌ Book not found.\n")
