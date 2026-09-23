# Contact Book Application
# Python Essentials Project

import json
import os

filename = "contacts.json"

def get_contacts():
    if os.path.exists(filename):
        try:
            with open(filename, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

def save_all_contacts(data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def add_new_contact():
    print("\n--- Add New Contact ---")
    name = input("Enter contact name: ").strip().title()
    if name == "":
        print("Error: Name cannot be blank.")
        return
    
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()

    contacts = get_contacts()
    
    # Store contact details in a dictionary
    contacts[name] = {
        "phone": phone,
        "email": email
    }
    
    save_all_contacts(contacts)
    print("Contact for " + name + " saved successfully.")

def show_all_contacts():
    contacts = get_contacts()
    if not contacts:
        print("\nNo contacts saved yet.")
        return

    print("\n---------------- Contact List ----------------")
    for name, details in contacts.items():
        p = details.get("phone", "N/A")
        e = details.get("email", "N/A")
        print(f"Name: {name} | Phone: {p} | Email: {e}")
    print("----------------------------------------------")

def find_contact():
    query = input("\nEnter name to search: ").strip().title()
    contacts = get_contacts()
    
    if query in contacts:
        p = contacts[query]["phone"]
        e = contacts[query]["email"]
        print(f"\nFound Record:\nName: {query}\nPhone: {p}\nEmail: {e}")
    else:
        print(f"\nNo contact found with the name '{query}'.")

def remove_contact():
    name_to_del = input("\nEnter name to delete: ").strip().title()
    contacts = get_contacts()
    
    if name_to_del in contacts:
        del contacts[name_to_del]
        save_all_contacts(contacts)
        print(f"Successfully deleted {name_to_del}.")
    else:
        print(f"Could not find {name_to_del} to delete.")

def main():
    while True:
        print("\n=== CONTACT BOOK MENU ===")
        print("1. Add Contact")
        print("2. Display All Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        
        option = input("Enter option (1-5): ").strip()

        if option == "1":
            add_new_contact()
        elif option == "2":
            show_all_contacts()
        elif option == "3":
            find_contact()
        elif option == "4":
            remove_contact()
        elif option == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid input. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()