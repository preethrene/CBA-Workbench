from utils import init_file
from add_employee import add_employee
from view_employees import view_employees
from search_department import search_department
from update_salary import update_salary
from delete_employee import delete_employee

def menu():
    init_file()
    while True:
        print("\n====== Employee Directory ======")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search Employees by Department")
        print("4. Update Salary")
        print("5. Delete Employee")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_employee()
        elif choice == '2':        
            view_employees()
        elif choice == '3':
            search_department()
        elif choice == '4':
            update_salary()
        elif choice == '5':
            delete_employee()
        elif choice == '6':
            print("\n👋 Exiting... Data saved in employees.csv\n")
            break
        else:
            print("\n⚠️ Invalid choice! Try again.\n")

if __name__ == "__main__":
    menu()
