from utils import init_file
from add_book import add_book
from view_books import view_books
from search_books import search_books
from update_status import update_status
from delete_book import delete_book

def menu():
    init_file()
    while True:
        print("\n====== 📚 Library Book Records ======")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Search Books by Title/Author")
        print("4. Update Book Status (Borrow/Return)")
        print("5. Delete Book")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_book()
        elif choice == '2':
            view_books()
        elif choice == '3':
            search_books()
        elif choice == '4':
            update_status()
        elif choice == '5':
            delete_book()
        elif choice == '6':
            print("\n👋 Exiting... Data saved in books.csv\n")
            break
        else:
            print("\n⚠️ Invalid choice! Try again.\n")

if __name__ == "__main__":
    menu()
