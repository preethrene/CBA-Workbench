import csv
from utils import FILE_NAME

def add_employee():
    empid = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    dept = input("Enter Department: ")
    salary = input("Enter Salary: ")
    contact = input("Enter Contact: ")

    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([empid, name, dept, salary, contact])

    print("\n✅ Employee added successfully!\n")
