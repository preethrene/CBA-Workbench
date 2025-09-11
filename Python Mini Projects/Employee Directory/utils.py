import csv
import os

FILE_NAME = "employees.csv"

# Ensure CSV file exists with headers
def init_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["EmpID", "Name", "Department", "Salary", "Contact"])
