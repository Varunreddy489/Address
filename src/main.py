from AddressBook import AddressBook


class AddressBookMain:
    @staticmethod
    def start():
        print("\nWelcome to the Address Book Program!")
        AddressBookMain.address_books = {}

    def menu(self):
        print(
            "\nMenu:\n1. Add new Contact\n2. Display Contacts\n3. Edit Contact\n4. Delete Contact\n5. Exit"
        )
        try:
            option = int(input("Enter option: "))
            match option:
                case 1:
                    details = {}
                    print("\nEnter contact details:")
                    details["first_name"] = input("First name: ").strip()
                    details["last_name"] = input("Last name: ").strip()
                    details["email"] = input("Email: ").strip()
                    details["phone_number"] = input("Phone number: ").strip()
                    details["address"] = input("Address: ").strip()
                    details["city"] = input("City: ").strip()
                    details["state"] = input("State: ").strip()
                    details["zip_code"] = input("Zip Code: ").strip()

                    address_book_name = input(
                        "\nPlease Enter Address Book Name: "
                    ).strip()
                    try:
                        if address_book_name not in AddressBookMain.address_books:
                            AddressBookMain.address_books[address_book_name] = (
                                AddressBook(address_book_name)
                            )
                        ab = AddressBookMain.address_books[address_book_name]

                        ab.add_contact(**details)
                        print("Contact added successfully.")
                        print(f"Current contacts in {address_book_name}:")
                        for contact in ab.contacts:
                            print(f"{contact.first_name} {contact.last_name}")
                    except ValueError as e:
                        print(e)

                case 2:
                    address_book_name = input(
                        "Enter Address Book Name to display: "
                    ).strip()
                    if address_book_name in AddressBookMain.address_books:
                        ab = AddressBookMain.address_books[address_book_name]
                        print(f"\nContacts in {address_book_name}:")
                        for contact in ab.contacts:
                            print(f"\nName: {contact.first_name} {contact.last_name}")
                            print(f"Email: {contact.email}")
                            print(f"Phone: {contact.phone_number}")
                            print(
                                f"Address: {contact.address}, {contact.city}, {contact.state} {contact.zip_code}"
                            )
                    else:
                        print(f"Address book '{address_book_name}' not found.")

                case 3:
                    address_book_name = input("Enter Address Book Name: ").strip()
                    if address_book_name in AddressBookMain.address_books:
                        ab = AddressBookMain.address_books[address_book_name]
                        first_name = input(
                            "\nEnter the first name of the contact to edit: "
                        ).strip()
                        last_name = input(
                            "Enter the last name of the contact to edit: "
                        ).strip()

                        print(f"\nAvailable contacts in {address_book_name}:")
                        for contact in ab.contacts:
                            print(f"- {contact.first_name} {contact.last_name}")

                        contact = ab.find_contact(first_name, last_name)
                        if contact:
                            print(f"\nCurrent details for {first_name} {last_name}:")
                            print(f"Email: {contact.email}")
                            print(f"Phone: {contact.phone_number}")
                            print(
                                f"Address: {contact.address}, {contact.city}, {contact.state} {contact.zip_code}"
                            )

                            field = input(
                                "\nEnter the field to edit (e.g., phone_number, address, city, email): "
                            ).strip()
                            new_value = input(f"Enter new value for {field}: ").strip()
                            ab.edit_contact(first_name, last_name, field, new_value)
                            print("Contact updated successfully.")
                        else:
                            print(
                                f"Contact '{first_name} {last_name}' not found in this address book."
                            )
                    else:
                        print(f"Address book '{address_book_name}' not found.")

                case 4:
                    address_book_name = input("Enter Address Book Name: ").strip()
                    if address_book_name in AddressBookMain.address_books:
                        ab = AddressBookMain.address_books[address_book_name]
                        first_name = input(
                            "Enter first name of contact to delete: "
                        ).strip()
                        last_name = input(
                            "Enter last name of contact to delete: "
                        ).strip()
                        contact = ab.find_contact(first_name, last_name)
                        if contact:
                            ab.contacts.remove(contact)
                            print("Contact deleted successfully.")
                        else:
                            print("Contact not found.")
                    else:
                        print(f"Address book '{address_book_name}' not found.")

                case 5:
                    exit()
        except ValueError:
            print("\nInvalid option. Please try again.")


if __name__ == "__main__":
    app = AddressBookMain()
    app.start()
    while True:
        app.menu()
