from db.db_config import connect_db


class AddressBook:

    def __init__(self,  address_book_id):
        self.contacts = []
        self.address_book_id = address_book_id
        self.people_in_city = {}
        self.people_in_state = {}

    def is_duplicate(self, first_name, last_name):
        for contact in self.contacts:
            if contact.first_name == first_name and contact.last_name == last_name:
                return True
        return False

    def handle_add_contact(self, contact_details: dict):
        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO contacts (address_book_id, first_name, last_name, email, phone_number, address, city, state, zip_code) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (
            1,
            contact_details["first_name"],
            contact_details["last_name"],
            contact_details["email"],
            contact_details["phone_number"],
            contact_details["address"],
            contact_details["city"],
            contact_details["state"],
            contact_details["zip_code"],
            ),
        )
        conn.commit()
        cursor.close()
        conn.close()

    def find_contact(self, first_name, last_name):
        for contact in self.contacts:
            if contact.first_name == first_name and contact.last_name == last_name:
                return contact
        return None

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
