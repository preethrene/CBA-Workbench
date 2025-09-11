import csv
from utils import FILE_NAME

def search_books():
    keyword = input("Enter Title or Author to Search: ").lower()
    found = False
    with open(FILE_NAME, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if keyword in row['Title'].lower() or keyword in row['Author'].lower():
                print(f"ID: {row['BookID']} | Title: {row['Title']} | Author: {row['Author']} | Year: {row['Year']} | Status: {row['Status']}")
                found = True
    if not found:
        print("\n❌ No matching books found.\n")

