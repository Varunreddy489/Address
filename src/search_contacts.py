from collections import defaultdict


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

    def count_contacts_by_city_or_state(self):
        option = input("Count by (1) City or (2) State? Enter 1 or 2: ").strip()
        count_map = defaultdict(int)

        for ab in self.address_books.values():
            for contact in ab.contacts:
                key = contact.city if option == "1" else contact.state
                count_map[key] += 1

        if not count_map:
            print("No contacts found.")
            return

        print("\nContact Counts:")
        for location, count in count_map.items():
            print(f"{location}: {count} contact(s)")

    def _display_contact(self, contact):
        print(f"\nName: {contact.first_name} {contact.last_name}")
        print(f"Email: {contact.email}")
        print(f"Phone: {contact.phone_number}")
        print(
            f"Address: {contact.address}, {contact.city}, {contact.state} {contact.zip_code}"
        )
