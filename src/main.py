from AddressBook import AddressBook
from db.db_config import connect_db
from search_contacts import SearchContacts


class Main:
    address_books = {}

    curr = connect_db()

    @staticmethod
    def start():
        print("\nWelcome to the Address Book Program!")

    def add_contact(self):
        ab_name = input("\nPlease Enter Address Book Name: ")
        ab = self.get_address_book(ab_name)

        contact_details = self.get_contact_details()
        if ab.is_duplicate(contact_details["first_name"], contact_details["last_name"]):
            print("Duplicate entry found!")
            return
        print(ab, contact_details)
        ab.handle_add_contact(contact_details)


    def get_contact_details(self) -> dict:
        """Prompt user for contact details"""
        print("\nEnter contact details:")
        return {
            "first_name": input("First name: "),
            "last_name": input("Last name: "),
            "email": input("Email: "),
            "phone_number": input("Phone number: "),
            "address": input("Address: "),
            "city": input("City: "),
            "state": input("State: "),
            "zip_code": input("Zip Code: "),
        }

    def get_address_book(self, name) -> AddressBook:
        """Get or create an address book by name"""
        name = name.strip()
        if name not in self.address_books:
            self.address_books[name] = AddressBook(name)
        return self.address_books[name]
    
    def display_contact(self, contact):
        """Display a single contact's details"""
        print(f"\nName: {contact.first_name} {contact.last_name}")
        print(f"Email: {contact.email}")
        print(f"Phone: {contact.phone_number}")
        print(
            f"Address: {contact.address}, {contact.city}, {contact.state} {contact.zip_code}"
        )

    def display_contacts(self):
        """Handle the contact display workflow with alphabetical sorting"""
        ab_name = input("Enter Address Book Name to display: ").strip()
        if ab_name in self.address_books:
            ab = self.address_books[ab_name]
            if not ab.contacts:
                print("\n No contacts found in this address book.")
                return

            print(f"\nContacts in {ab_name} (sorted alphabetically):")
            for contact in sorted(
                ab.contacts, key=lambda c: (c.first_name.lower(), c.last_name.lower())
            ):
                self.display_contact(contact)
        else:
            print(f"Address book '{ab_name}' not found.")

    def edit_contact(self):
        """Handle the contact editing workflow"""
        ab_name = input("Enter Address Book Name: ").strip()
        if ab_name not in self.address_books:
            print(f"Address book '{ab_name}' not found.")
            return

        ab = self.address_books[ab_name]
        first_name = input("\nEnter first name of contact to edit: ").strip()
        last_name = input("Enter last name of contact to edit: ").strip()

        contact = ab.find_contact(first_name, last_name)
        if not contact:
            print(f"Contact '{first_name} {last_name}' not found.")
            return

        self.display_contact(contact)
        field = input("\nEnter field to edit: ").strip()
        new_value = input(f"Enter new value for {field}: ").strip()

        try:
            ab.edit_contact(first_name, last_name, field, new_value)
            print("Contact updated successfully.")
        except ValueError as e:
            print(f"Error: {e}")

    def delete_contact(self):
        """Handle the contact deletion workflow"""
        ab_name = input("Enter Address Book Name: ").strip()
        if ab_name not in self.address_books:
            print(f"Address book '{ab_name}' not found.")
            return

        ab = self.address_books[ab_name]
        first_name = input("Enter first name of contact to delete: ").strip()
        last_name = input("Enter last name of contact to delete: ").strip()

        contact = ab.find_contact(first_name, last_name)
        if contact:
            ab.contacts.remove(contact)
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")

    def add_address_books(self):
        """Handle the address book addition workflow"""

        while True:
            ab_name = input("Enter new Address Book name: ")
            if ab_name in self.address_books:
                print(f"Address book '{ab_name}' already exists.")
            else:
                self.address_books[ab_name] = AddressBook(ab_name)
                print(f"Address book '{ab_name}' created successfully.")

            if input("Add another Address Book? (yes/no): ") != "y":
                break

    def search_contacts(self):
        """Handle the contact search workflow"""
        ab_name = input("Enter Address Book Name to search: ").strip()
        if ab_name not in self.address_books:
            print(f"Address book '{ab_name}' not found.")
            return

        city_or_state = input("Enter city or state to search: ").strip()
        search_results = SearchContacts(
            self.address_books[ab_name]
        ).search_all_address_books(city_or_state)

        if not search_results:
            print("No contacts found.")
            return

        print("\nSearch Results:")
        for contact in search_results:
            self.display_contact(contact)

    def search_contacts_by_city(self):
        """Search City to SearchContacts"""
        SearchContacts(self.address_books).search_by_city()

    def search_contacts_by_state(self):
        """Search State to SearchContacts"""
        SearchContacts(self.address_books).search_by_state()

    def count_contacts_by_city_or_state(self):
        """Count contacts by city or state"""
        SearchContacts(self.address_books).count_contacts_by_city_or_state()

    def sort_contacts_by_city_or_state_or_zip(self):
        """Sort contacts by city or state"""
        ab_name = input("Enter Address Book Name to display: ").strip()
        if ab_name not in self.address_books:
            print(f"Address book '{ab_name}' not found.")
            return

        ab = self.address_books[ab_name]
        if not ab.contacts:
            print("\nNo contacts found in this address book.")
            return

        print("\nSort contacts by:")
        print("1. City")
        print("2. State")
        print("3. Zip Code")

        sort_option = input("Enter choice (1-4): ").strip()

        if sort_option == "1":
            sorted_contacts = sorted(ab.contacts, key=lambda c: c.city.lower())
        elif sort_option == "2":
            sorted_contacts = sorted(ab.contacts, key=lambda c: c.state.lower())
        elif sort_option == "3":
            sorted_contacts = sorted(ab.contacts, key=lambda c: c.zip_code)
        else:
            print("Invalid choice. Showing unsorted contacts.")
            sorted_contacts = ab.contacts

        print(f"\nContacts in {ab_name} (sorted):")
        for contact in sorted_contacts:
            self.display_contact(contact)

    def menu(self):
        """Main menu handler"""
        options = {
            0: ("Exit", exit),
            1: ("Add new Contact", self.add_contact),
            2: ("Display Contacts", self.display_contacts),
            3: ("Edit Contact", self.edit_contact),
            4: ("Delete Contact", self.delete_contact),
            5: ("Add Address Books", self.add_address_books),
            6: ("Search Contacts", self.search_contacts),
            7: ("Search Contacts By City", self.search_contacts_by_city),
            8: ("Search Contacts By State", self.search_contacts_by_state),
            9: (
                "Count Contacts by City or State",
                self.count_contacts_by_city_or_state,
            ),
            10: (
                "Sort Contacts by City or State",
                self.sort_contacts_by_city_or_state_or_zip,
            ),
        }

        while True:
            print("\nMenu:")
            for num, (text, _) in options.items():
                print(f"{num}. {text}")

            try:
                option = int(input("Enter option: "))
                if option in options:
                    options[option][1]()
                else:
                    print("Invalid option. Please try again.")
            except ValueError:
                print("Please enter a valid number.")


if __name__ == "__main__":
    app = Main()
    app.start()
    app.menu()
