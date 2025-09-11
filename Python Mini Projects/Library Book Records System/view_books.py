import csv
from utils import FILE_NAME

def view_books():
    with open(FILE_NAME, mode="r") as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        if not rows:
            print("\n⚠️ No book records found.\n")
            return
        print("\n📚 Library Book Records:")
        print("-" * 70)
        for row in rows:
            print(f"ID: {row['BookID']} | Title: {row['Title']} | Author: {row['Author']} | Year: {row['Year']} | Status: {row['Status']}")
        print("-" * 70)
