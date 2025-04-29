import re
import json
import random
from faker import Faker

faker = Faker()

# Regex patterns
address_book_id_pattern = r"^\d{1,}$"
first_name_pattern = r"^[A-Z][a-z]{1,}$"
last_name_pattern = r"^[A-Z][a-z]{1,}$"
address_pattern = r"^.{10,}$"
city_pattern = r"^[A-Za-z\s]{2,}$"
state_pattern = r"^[A-Za-z\s]{2,}$"
zip_code_pattern = r"^\d{6}$"
phone_pattern = r"^[6-9][0-9]{9}$"
email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w{2,}$"


def validate(value, pattern: str, error_message: str):
    """Validate the value against the regex pattern."""
    if not re.match(pattern, str(value)):
        raise ValueError(error_message)
    return value


def generate_contact():
    """Generate a single contact with validated data"""
    try:
        contact = {
            "address_book_id": validate(
                random.randint(1, 10),
                address_book_id_pattern,
                "Invalid address book id",
            ),
            "first_name": validate(
                faker.first_name(), first_name_pattern, "Invalid first name"
            ),
            "last_name": validate(
                faker.last_name(), last_name_pattern, "Invalid last name"
            ),
            "email": validate(faker.email(), email_pattern, "Invalid email"),
            "phone_number": validate(
                str(random.randint(6000000000, 9999999999)),
                phone_pattern,
                "Invalid phone number",
            ),
            "address": validate(
                faker.address().replace("\n", ", "), address_pattern, "Invalid address"
            ),
            "city": validate(faker.city(), city_pattern, "Invalid city"),
            "state": validate(faker.state(), state_pattern, "Invalid state"),
            "zip_code": validate(
                str(random.randint(100000, 999999)),
                zip_code_pattern,
                "Invalid zip code",
            ),
        }
        return contact
    except ValueError as e:
        print(f"Validation error: {e}")
        return None


def generate_contacts(num_contacts: int = 100000):
    """Generate multiple contacts and save to JSON file"""
    with open("contacts.json", "w") as f:
        for _ in range(num_contacts):
            contact = generate_contact()
            if contact:  # Only write valid contacts
                json.dump(contact, f)
                f.write("\n")
    print(f"Successfully generated {num_contacts} contacts")


if __name__ == "__main__":
    generate_contacts()
