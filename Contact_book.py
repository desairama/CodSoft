# Global variable to store contacts
contacts = []

# Function to add a new contact
def add_contact(name, phone, email, address):
    contacts.append({"Name": name, "Phone": phone, "Email": email, "Address": address})
    print("Contact added successfully!")

# Function to display all contacts
def view_contacts():
    if contacts:
        print("Contacts:")
        for contact in contacts:
            print(f"Name: {contact['Name']}, Phone: {contact['Phone']}, Email: {contact['Email']}, Address: {contact['Address']}")
    else:
        print("No contacts to display.")

# Function to search for a contact by name or phone number
def search_contact(search_term):
    search_result = []
    for contact in contacts:
        if search_term in contact['Name'].lower() or search_term in contact['Phone']:
            search_result.append(contact)
    if search_result:
        print("Search Results:")
        for contact in search_result:
            print(f"Name: {contact['Name']}, Phone: {contact['Phone']}, Email: {contact['Email']}, Address: {contact['Address']}")
    else:
        print("No matching contacts found.")

# Function to update contact details
def update_contact(name, new_phone, new_email, new_address):
    for contact in contacts:
        if contact['Name'] == name:
            contact['Phone'] = new_phone
            contact['Email'] = new_email
            contact['Address'] = new_address
            print("Contact details updated successfully!")
            return
    print("Contact not found.")

# Function to delete a contact
def delete_contact(name):
    for contact in contacts:
        if contact['Name'] == name:
            contacts.remove(contact)
            print("Contact deleted successfully!")
            return
    print("Contact not found.")

# Main menu
def main_menu():
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

# Main function to handle user input and operations
def main():
    while True:
        main_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            address = input("Enter address: ")
            add_contact(name, phone, email, address)

        elif choice == '2':
            view_contacts()

        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            search_contact(search_term.lower())

        elif choice == '4':
            name = input("Enter name of contact to update: ")
            new_phone = input("Enter new phone number: ")
            new_email = input("Enter new email address: ")
            new_address = input("Enter new address: ")
            update_contact(name, new_phone, new_email, new_address)

        elif choice == '5':
            name = input("Enter name of contact to delete: ")
            delete_contact(name)

        elif choice == '6':
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice! Please enter a valid option.")

if __name__ == "__main__":
    main()
