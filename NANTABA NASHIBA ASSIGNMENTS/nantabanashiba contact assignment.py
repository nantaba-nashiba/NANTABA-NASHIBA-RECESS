import re


class ContactManager:
    def __init__(self):
        self.contacts = []

    @staticmethod
    def validate_phone(phone: str) -> bool:
        if not phone:
            return False
        return bool(re.fullmatch(r"\+?[0-9-]+", phone))

    @staticmethod
    def validate_email(email: str) -> bool:
        return bool(email and "@" in email and "." in email)

    def find_contact_index(self, name: str):
        normalized = name.strip().lower()
        for index, contact in enumerate(self.contacts):
            if contact["name"].lower() == normalized:
                return index
        return None

    def add_contact(self, name: str, phone: str, email: str = "") -> bool:
        name = name.strip()
        phone = phone.strip()
        email = email.strip()

        if not name:
            print("Error: Name is required.")
            return False

        if not self.validate_phone(phone):
            print("Error: Phone number may only contain digits, hyphens, and an optional leading '+'.")
            return False

        if email and not self.validate_email(email):
            print("Error: Email must contain an '@' symbol and a '.'.")
            return False

        if self.find_contact_index(name) is not None:
            print(f"Error: A contact named '{name}' already exists.")
            return False

        self.contacts.append({"name": name, "phone": phone, "email": email})
        print(f"Contact '{name}' added successfully.")
        return True

    def view_contact(self, name: str) -> None:
        index = self.find_contact_index(name)
        if index is None:
            print(f"Contact '{name}' not found.")
            return

        self.display_contacts([self.contacts[index]])

    def update_contact(self, name: str, phone: str = None, email: str = None) -> bool:
        index = self.find_contact_index(name)
        if index is None:
            print(f"Contact '{name}' not found.")
            return False

        contact = self.contacts[index]

        if phone is not None:
            phone = phone.strip()
            if phone and not self.validate_phone(phone):
                print("Error: Phone number may only contain digits, hyphens, and an optional leading '+'.")
                return False
            if phone:
                contact["phone"] = phone

        if email is not None:
            email = email.strip()
            if email and not self.validate_email(email):
                print("Error: Email must contain an '@' symbol and a '.'.")
                return False
            contact["email"] = email

        print(f"Contact '{name}' updated successfully.")
        self.display_contacts([contact])
        return True

    def delete_contact(self, name: str) -> bool:
        index = self.find_contact_index(name)
        if index is None:
            print(f"Contact '{name}' not found.")
            return False

        removed = self.contacts.pop(index)
        print(f"Contact '{removed['name']}' deleted successfully.")
        return True

    def search_contacts(self, query: str):
        normalized = query.strip().lower()
        return [
            contact
            for contact in self.contacts
            if normalized in contact["name"].lower()
            or normalized in contact["phone"].lower()
            or normalized in contact["email"].lower()
        ]

    def list_contacts(self):
        return self.contacts

    @staticmethod
    def format_contact(contact: dict) -> str:
        email = contact["email"] or "(no email)"
        return f"Name: {contact['name']} | Phone: {contact['phone']} | Email: {email}"

    def display_contacts(self, contacts: list) -> None:
        if not contacts:
            print("No contacts found.")
            return

        print("\n--- Contact Results ---")
        for index, contact in enumerate(contacts, start=1):
            print(f"{index}. {self.format_contact(contact)}")
        print("--- End of Results ---\n")


def main():
    manager = ContactManager()

    while True:
        print("=== Contact Manager Menu ===")
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Search Contacts")
        print("6. List All Contacts")
        print("7. Exit")

        choice = input("Choose an option (1-7): ").strip()
        print()

        if choice == "1":
            name = input("Enter name: ").strip()
            phone = input("Enter phone: ").strip()
            email = input("Enter email (optional): ").strip()
            manager.add_contact(name, phone, email)

        elif choice == "2":
            name = input("Enter the name of the contact to view: ").strip()
            manager.view_contact(name)

        elif choice == "3":
            name = input("Enter the name of the contact to update: ").strip()
            if not name:
                print("Name is required to update a contact.")
                continue
            phone = input("Enter new phone (leave blank to keep current): ").strip()
            email = input("Enter new email (leave blank to keep current or clear): ").strip()
            phone_arg = phone if phone else None
            email_arg = email if email else None
            manager.update_contact(name, phone=phone_arg, email=email_arg)

        elif choice == "4":
            name = input("Enter the name of the contact to delete: ").strip()
            manager.delete_contact(name)

        elif choice == "5":
            query = input("Enter name, phone, or email to search: ").strip()
            results = manager.search_contacts(query)
            manager.display_contacts(results)

        elif choice == "6":
            all_contacts = manager.list_contacts()
            manager.display_contacts(all_contacts)

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

        print()


if __name__ == "__main__":
    main()
