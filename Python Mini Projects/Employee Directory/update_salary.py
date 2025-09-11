import csv
from utils import FILE_NAME

def update_salary():
    empid = input("Enter Employee ID to Update Salary: ")
    updated = False
    rows = []

    with open(FILE_NAME, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['EmpID'] == empid:
                new_salary = input("Enter New Salary: ") or row['Salary']
                row['Salary'] = new_salary
                updated = True
            rows.append(row)

    if updated:
        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["EmpID", "Name", "Department", "Salary", "Contact"])
            writer.writeheader()
            writer.writerows(rows)
        print("\n✅ Salary updated successfully!\n")
    else:
        print("\n❌ Employee not found.\n")
