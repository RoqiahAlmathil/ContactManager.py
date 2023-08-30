class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}\nPhone: {self.phone}\nEmail: {self.email}"


class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def remove_contact(self, contact):
        if contact in self.contacts:
            self.contacts.remove(contact)

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                return contact
        return None

    def display_all_contacts(self):
        for contact in self.contacts:
            print(contact)
            print("--------------------")


# Function to display the menu and get user's choice
def display_menu():
    print("Contact Manager Menu:")
    print("1. Add a contact")
    print("2. Remove a contact")
    print("3. Search for a contact")
    print("4. Display all contacts")
    print("5. Exit")
    choice = input("Enter your choice : ")
    return choice

manager = ContactManager()

while True:
    choice = display_menu()

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email address: ")
        contact = Contact(name, phone, email)
        manager.add_contact(contact)
        print("Contact added successfully!")

    elif choice == "2":
        name = input("Enter name to remove: ")
        contact = manager.search_contact(name)
        if contact:
            manager.remove_contact(contact)
            print("Contact removed successfully!")
        else:
            print(f"No contact found with the name {name}")

    elif choice == "3":
        name = input("Enter name to search: ")
        contact = manager.search_contact(name)
        if contact:
            print(f"Contact found:\n{contact}")
        else:
            print(f"No contact found with the name {name}")

    elif choice == "4":
        manager.display_all_contacts()

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice! Please try again.")