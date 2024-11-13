# Contact Manager 
class Contact:
    def __init__(self, name, phone, email): #Assigning variables
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}\nPhone: {self.phone}\nEmail: {self.email}"


def menu():
    contact_manager = ContactManager()
    
    while True:
        print("\nContact Manager Menu:")
        print("1. Add a Contact")
        print("2. View a Contact")
        print("3. Update a Contact")
        print("4. Delete a Contact")
        print("5. View all the Contacts")
        print("6. Exit")
        
        choice = input("Choose any option (1-6): ") # Taking user input
        
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            contact_manager.add_contact(name, phone, email)
        
        elif choice == '2':
            name = input("Enter the name of the contact to view: ")
            contact_manager.view_contact(name)
        
        elif choice == '3':
            name = input("Enter the name of the contact to update: ")
            phone = input("Enter a new phone number (press Enter to skip): ")
            email = input("Enter a new email address (press Enter to skip): ")
            contact_manager.update_contact(name, phone if phone else None, email if email else None)
        
        elif choice == '4':
            name = input("Enter the name of the contact to delete: ")
            contact_manager.delete_contact(name)
        
        elif choice == '5':
            contact_manager.display_all_contacts()
        
        elif choice == '6':
            print("Exit Contact Manager...")
            break
        
        else:
            print("Invalid option. Please try again.")
class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email):
        if name in self.contacts:
            print(f"Contact with this name {name} already exist.")
        else:
            self.contacts[name] = Contact(name, phone, email)
            print(f"Contact {name} is successfully added.")

    def view_contact(self, name):
        if name in self.contacts:
            print(self.contacts[name])
        else:
            print(f"Contact {name} not found.")

    def update_contact(self, name, phone=None, email=None):
        if name in self.contacts:
            if phone:
                self.contacts[name].phone = phone
            if email:
                self.contacts[name].email = email
            print(f"Contact {name} is successfully updated.")
        else:
            print(f"Contact {name} not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact {name} is successfully deleted.")
        else:
            print(f"Contact {name} doesn't exist.")

    def display_all_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for contact in self.contacts.values():
                print(contact)
                print("-" * 20)
            

if __name__ == "__main__":
    menu()