import csv
from utils import FILE_NAME

def delete_book():
    bookid = input("Enter Book ID to Delete: ")
    deleted = False
    rows = []

    with open(FILE_NAME, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['BookID'] == bookid:
                deleted = True
            else:
                rows.append(row)

    if deleted:
        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["BookID", "Title", "Author", "Year", "Status"])
            writer.writeheader()
            writer.writerows(rows)
        print("\n Book deleted successfully!\n")
    else:
        print("\n❌ Book not found.\n")
