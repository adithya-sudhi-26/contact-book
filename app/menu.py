# app/menu.py
from app.operations import add_new_contact, show_all_contacts, find_contact, remove_contact

def display_main_menu():
    while True:
        print("\n=== CONTACT BOOK MENU ===")
        print("1. Add Contact")
        print("2. Display All Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        
        user_choice = input("Enter option (1-5): ").strip()

        if user_choice == "1":
            add_new_contact()
        elif user_choice == "2":
            show_all_contacts()
        elif user_choice == "3":
            find_contact()
        elif user_choice == "4":
            remove_contact()
        elif user_choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid input. Please enter a number between 1 and 5.")