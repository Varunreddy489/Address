from utils.utils import validate_contact
from Contact import Contact


class AddressBook:
    def __init__(self, address_book_name):
        self.address_book_name = address_book_name
        self.contacts = []

    @validate_contact
    def add_contact(self, **kwargs):
        contact = Contact(
            kwargs["first_name"],
            kwargs["last_name"],
            kwargs["phone_number"],
            kwargs["address"],
            kwargs["city"],
            kwargs["state"],
            kwargs["zip"],
            kwargs["email"],
        )
        self.contacts.append(contact)

        print("Contact added successfully.")
