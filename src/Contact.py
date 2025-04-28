class Contact:
    def __init__(
        self, first_name, last_name, phone_number, address, city, state, zip, email
    ):
        self.first_name = None
        self.last_name = None
        self.address = None
        self.city = None
        self.state = None
        self.zip_code = None
        self.phone_number = None
        self.email = None

    def __repr__(self):
        return (
            f"Contact({self.first_name}, {self.last_name}, {self.address}, "
            f"{self.city}, {self.state}, {self.zip_code}, {self.phone_number}, {self.email})"
        )
