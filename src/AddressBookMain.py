import AddressBook


class AddressBookMain:
    def __init__(self):
        self.address_books = {}

    def add_address_book(self, name):
        """
        Function to create a new address book
        """
        self.address_books[name] = AddressBook(name)
        print(f"\nSuccessfully created Address Book - {name}")

    def get_all_address_books(self):
        """
        To get all address books
        """
        return self.address_books
