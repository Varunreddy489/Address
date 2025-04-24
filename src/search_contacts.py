class SearchContacts:
    def __init__(self, address_books):
        self.address_books = address_books

    def search_all_address_books(self, city_or_state):
        search_results = []
        for name, address_book in self.address_books.items():
            for contact in address_book.contacts:
                if (
                    contact.city.lower() == city_or_state.lower()
                    or contact.state.lower() == city_or_state.lower()
                ):
                    search_results.append(contact)
        return search_results

    def search_by_city(self):
        ab_name = input("Enter Address Book Name to search: ").strip()
        if ab_name not in self.address_books:
            print(f"Address book '{ab_name}' not found.")
            return

        city = input("Enter city to search: ").strip()
        search_results = self.search_all_address_books(city)

        if not search_results:
            print("No contacts found.")
            return

        print("\nSearch Results:")
        for contact in search_results:
            self._display_contact(contact)

    def search_by_state(self):
        ab_name = input("Enter Address Book Name to search: ").strip()
        if ab_name not in self.address_books:
            print(f"Address book '{ab_name}' not found.")
            return

        state = input("Enter state to search: ").strip()
        search_results = self.search_all_address_books(state)

        if not search_results:
            print("No contacts found.")
            return

        print("\nSearch Results:")
        for contact in search_results:
            self._display_contact(contact)

    def _display_contact(self, contact):
        print(f"\nName: {contact.first_name} {contact.last_name}")
        print(f"Email: {contact.email}")
        print(f"Phone: {contact.phone_number}")
        print(
            f"Address: {contact.address}, {contact.city}, {contact.state} {contact.zip_code}"
        )
