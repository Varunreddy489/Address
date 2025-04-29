import os
import csv
import json


def save_contact_to_txt_file(self, contact_details, ab_name):
    """Save contact details to a txt file"""
    file_name = f"{ab_name}_contacts.txt"
    with open(file_name, "a") as file:
        file.write(f"\nContact in Address Book '{ab_name}':\n")
        file.write(
            f"Name: {contact_details['first_name']} {contact_details['last_name']}\n"
        )
        file.write(f"Email: {contact_details['email']}\n")
        file.write(f"Phone: {contact_details['phone_number']}\n")
        file.write(
            f"Address: {contact_details['address']}, {contact_details['city']}, {contact_details['state']} {contact_details['zip_code']}\n"
        )
        file.write("-" * 50 + "\n")


def save_contact_to_csv_file(self, contact_details, ab_name):
    """Save contact details to a CSV file"""
    file_name = f"{ab_name}_contacts.csv"
    file_exists = os.path.exists(file_name)

    with open(file_name, "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=contact_details.keys())

        if not file_exists:
            writer.writeheader()

        writer.writerow(contact_details)


def save_contact_to_json_file(self, contact_details, ab_name):
    """Save contact details to a JSON file"""
    file_name = f"{ab_name}_contacts.json"

    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    data.append(contact_details)

    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)
