from utils import init_file
from add_item import add_item
from view_inventory import view_inventory
from search_item import search_item
from update_item import update_item
from delete_item import delete_item

def menu():
    init_file()
    while True:
        print("\n====== 📦 Inventory Management ======")
        print("1. Add New Item")
        print("2. View Stock Report")
        print("3. Search Item by Name")
        print("4. Update Quantity/Price")
        print("5. Delete Item")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_item()
        elif choice == '2':
            view_inventory()
        elif choice == '3':
            search_item()
        elif choice == '4':
            update_item()
        elif choice == '5':
            delete_item()
        elif choice == '6':
            print("\n👋 Exiting... Data saved in inventory.csv\n")
            break
        else:
            print("\n⚠️ Invalid choice! Try again.\n")

if __name__ == "__main__":
    menu()
