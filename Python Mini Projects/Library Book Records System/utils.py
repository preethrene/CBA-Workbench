import csv
import os

FILE_NAME = "books.csv"

# Ensure CSV file exists with headers
def init_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["BookID", "Title", "Author", "Year", "Status"])  # header row
