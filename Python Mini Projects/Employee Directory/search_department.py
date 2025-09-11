import csv
from utils import FILE_NAME

def search_department():
    dept = input("Enter Department to Search: ")
    found = False
    with open(FILE_NAME, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Department'].lower() == dept.lower():
                print(f"ID: {row['EmpID']} | Name: {row['Name']} | Salary: {row['Salary']} | Contact: {row['Contact']}")
                found = True
    if not found:
        print("\n❌ No employees found in this department.\n")
