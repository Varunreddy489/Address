import AddressBookMain


class SearchContacts(AddressBookMain):
    def __init__(self):
        super().__init__()
        self.address_books = {}

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
