from Contact import Contact
from utils.utils import validate_contact


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
            kwargs["zip_code"],
            kwargs["email"],
        )
        self.contacts.append(contact)

        print("Contact added successfully.")

    def find_contact(self, first_name, last_name):
        for contact in self.contacts:
            if contact.first_name == first_name and contact.last_name == last_name:
                return contact
        return None

    @validate_contact
    def edit_contact(self, first_name, last_name, field, new_value):
        contact = self.find_contact(first_name, last_name)
        if not contact:
            raise ValueError("Contact not found.")
        if not hasattr(contact, field):
            raise ValueError("Invalid field name.")
        setattr(contact, field, new_value)
        print(f"{field} updated successfully.")

    def delete_contact(self, first_name, last_name):
        contact = self.find_contact(first_name, last_name)
        if not contact:
            raise ValueError("Contact not found.")
        self.contacts.remove(contact)
        print("Contact deleted successfully.")
