import csv
from utils import FILE_NAME

def view_employees():
    with open(FILE_NAME, mode="r") as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        if not rows:
            print("\n⚠️ No employee records found.\n")
            return
        print("\n📋 Employee Directory:")
        print("-" * 60)
        for row in rows:
            print(f"ID: {row['EmpID']} | Name: {row['Name']} | Dept: {row['Department']} | Salary: {row['Salary']} | Contact: {row['Contact']}")
        print("-" * 60)
