import csv
import os

FILE_NAME = "inventory.csv"

# Ensure CSV file exists with headers
def init_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ItemID", "ItemName", "Quantity", "Price", "Supplier"])  # header row
