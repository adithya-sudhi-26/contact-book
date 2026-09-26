# app/operations.py
from app.storage import get_contacts, save_all_contacts

def add_new_contact():
    print("\n--- Add New Contact ---")
    name = input("Enter contact name: ").strip().title()
    if name == "":
        print("Error: Name cannot be blank.")
        return
    
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()

    contacts = get_contacts()
    contacts[name] = {"phone": phone, "email": email}
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