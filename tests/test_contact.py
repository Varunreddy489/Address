import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.AddressBook import AddressBook


@pytest.fixture
def sample_contact_data():
    """
    Fixture to provide sample contact data.
    """
    return [
        {
            "first_name": "Varun",
            "last_name": "Reddy",
            "phone_number": "91 8329392930",
            "address": "123 Street",
            "city": "Nellore",
            "state": "Andhra Pradesh",
            "zip": "1231223",
            "email": "varun@gmail.com",
        },
        {
            "first_name": "Varun",
            "last_name": "Reddy",
            "phone_number": "91 1231231231",
            "address": "Test Street",
            "city": "Chennai",
            "state": "Tamil Nadu",
            "zip": "123123",
            "email": "varun@gmail.com",
        },
    ]


@pytest.fixture
def sample_contact_book():
    """
    Fixture to create an address book object.
    """
    return AddressBook("contacts")


# ---------- Tests ----------


def test_add_valid_contact(sample_contact_data, sample_contact_book):
    """
    Test adding a single valid contact.
    """
    sample_contact_book.add_contact(**sample_contact_data[0])

    assert len(sample_contact_book.contacts) == 1
    assert sample_contact_book.contacts[0].first_name == "Varun"
    assert sample_contact_book.contacts[0].last_name == "Reddy"


def test_add_multiple_valid_contacts(sample_contact_data, sample_contact_book):
    """
    Test adding multiple valid contacts.
    """
    for data in sample_contact_data:
        sample_contact_book.add_contact(**data)

    assert len(sample_contact_book.contacts) == 2
    assert sample_contact_book.contacts[0].first_name == "Varun"
    assert sample_contact_book.contacts[1].last_name == "Reddy"


def test_add_invalid_contact(sample_contact_book):
    """
    Test adding a contact with invalid data.
    """
    invalid_contact = {
        "first_name": "Varun",
        "last_name": "Reddy",
        "phone_number": "invalid",  # Invalid phone number format
        "address": "123 Street",
        "city": "New York",
        "state": "NY",
        "zip": "12345",
        "email": "varun@example.com",
    }

    with pytest.raises(ValueError):
        sample_contact_book.add_contact(**invalid_contact)

    assert len(sample_contact_book.contacts) == 0


def test_edit_contact(sample_contact_data, sample_contact_book):
    """
    Test editing a contact's field.
    """
    for data in sample_contact_data:
        sample_contact_book.add_contact(**data)

    sample_contact_book.edit_contact("Varun", "email", "varunreddy@gmail.com", "Reddy")
    assert sample_contact_book.contacts[1].email == "varunreddy@gmail.com"


def test_invalid_edit_contact(sample_contact_data, sample_contact_book):
    """
    Test editing a contact with invalid value.
    """
    for data in sample_contact_data:
        sample_contact_book.add_contact(**data)

    with pytest.raises(ValueError):
        sample_contact_book.edit_contact(
            first_name="Varun", field="email", email="varunreddy.com", last_name="Reddy"
        )

    assert sample_contact_book.contacts[1].email != "varunreddy.com"


def test_delete_contact(sample_contact_data, sample_contact_book):
    """
    Test deleting a contact.
    """
    for data in sample_contact_data:
        sample_contact_book.add_contact(**data)

    sample_contact_book.delete_contact("Varun", "Reddy")
    assert len(sample_contact_book.contacts) == 1
    assert (
        sample_contact_book.contacts[0].last_name == "Reddy"
    )  # Only one should remain
