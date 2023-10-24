class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        for contact in self.contacts:
            print(f"Name: {contact.name}, Phone: {contact.phone}")

    def search_contact(self, search_term):
        for contact in self.contacts:
            if search_term in contact.name or search_term in contact.phone:
                print(f"Name: {contact.name}, Phone: {contact.phone}")

    def update_contact(self, name, new_phone, new_email, new_address):
        for contact in self.contacts:
            if contact.name == name:
                contact.phone = new_phone
                contact.email = new_email
                contact.address = new_address
                print("Contact updated successfully.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print("Contact deleted successfully.")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            address = input("Address: ")
            new_contact = Contact(name, phone, email, address)
            contact_book.add_contact(new_contact)
            print("Contact added successfully.")

        elif choice == "2":
            print("\nContact List:")
            contact_book.view_contacts()

        elif choice == "3":
            search_term = input("Enter name or phone number to search: ")
            contact_book.search_contact(search_term)

        elif choice == "4":
            name = input("Enter the name of the contact to update: ")
            new_phone = input("New Phone: ")
            new_email = input("New Email: ")
            new_address = input("New Address: ")
            contact_book.update_contact(name, new_phone, new_email, new_address)

        elif choice == "5":
            name = input("Enter the name of the contact to delete: ")
            contact_book.delete_contact(name)

        elif choice == "6":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
