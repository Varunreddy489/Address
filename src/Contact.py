class Contact:
    class Contact:
        def __init__(
            self,
            first_name,
            last_name,
            email,
            phone_number,
            address,
            city,
            state,
            zip_code,
        ):
            self.first_name = first_name
            self.last_name = last_name
            self.email = email
            self.phone_number = phone_number
            self.address = address
            self.city = city
            self.state = state
            self.zip_code = zip_code

        def __repr__(self):
            return (
                f"Contact({self.first_name}, {self.last_name}, {self.address}, "
                f"{self.city}, {self.state}, {self.zip_code}, {self.phone_number}, {self.email})"
            )
