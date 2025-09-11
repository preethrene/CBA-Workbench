import csv
from utils import FILE_NAME

def delete_employee():
    empid = input("Enter Employee ID to Delete: ")
    deleted = False
    rows = []

    with open(FILE_NAME, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['EmpID'] == empid:
                deleted = True
            else:
                rows.append(row)

    if deleted:
        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["EmpID", "Name", "Department", "Salary", "Contact"])
            writer.writeheader()
            writer.writerows(rows)
        print("\n Employee deleted successfully!\n")
    else:
        print("\n❌ Employee not found.\n")
