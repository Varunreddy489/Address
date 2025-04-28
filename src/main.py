from AddressBook import AddressBook


class AddressBookMain:
    @staticmethod
    def start():
        print("\nWelcome to the Address Book Program!")

    @staticmethod
    def menu():
        print(f"\nMenu:\n1. Add new Contact\n2. Display Contacts\n3. Exit")
        try:
            option = int(input("Enter option: "))
            match option:
                case 1:
                    details = {}
                    print("\nEnter contact details:")
                    details["first_name"] = input("First name: ")
                    details["last_name"] = input("Last name: ")
                    details["email"] = input("Email: ")
                    details["phone_number"] = input("Phone number: ")
                    details["address"] = input("Address: ")
                    details["city"] = input("City: ")
                    details["state"] = input("State: ")
                    details["zip"] = input("Zip Code: ")
                    address_book_name = input("\nPlease Enter Address Book Name: ")
                    try:
                        ab = AddressBook(address_book_name)
                        ab.add_contact(**details)
                    except ValueError as e:
                        print(e)

                case 2:
                    pass

                case 3:
                    exit()
        except ValueError:
            print("\nInvalid option. Please try again.")


if __name__ == "__main__":
    AddressBookMain.start()
    while True:
        AddressBookMain.menu()
