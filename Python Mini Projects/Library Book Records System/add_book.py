import csv
from utils import FILE_NAME

def add_book():
    bookid = input("Enter Book ID: ")
    title = input("Enter Title: ")
    author = input("Enter Author: ")
    year = input("Enter Year: ")
    status = "Available"  # default when adding a new book

    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([bookid, title, author, year, status])

    print("\n✅ Book added successfully!\n")
