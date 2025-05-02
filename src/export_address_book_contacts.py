import csv
from db.db_config import connect_db


def export_contacts_to_csv(address_book_name: str):
    conn = connect_db()
    cursor = conn.cursor(dictionary=True)

    try:
        cursor.execute(
            "SELECT id FROM address_books WHERE name = %s", (address_book_name,)
        )
        address_book = cursor.fetchone()

        if not address_book:
            print(f"Address book '{address_book_name}' not found.")
            return

        address_book_id = address_book["id"]
        print(f"Address Book ID: {address_book_id}")

        cursor.execute(
            """
            SELECT first_name, last_name, email, phone_number, address, city, state, zip_code
            FROM contacts
            WHERE address_book_id = %s
        """,
            (address_book_id,),
        )

        contacts = cursor.fetchall()
        print(contacts)

        if not contacts:
            print("No contacts found in the address book.")
            return

        safe_name = address_book_name.replace(" ", "_").lower()
        file_path = f"{safe_name}.csv"

        with open(file_path, mode="w", newline="", encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file)

            writer.writerow(
                [
                    "First Name",
                    "Last Name",
                    "Email",
                    "Phone Number",
                    "Address",
                    "City",
                    "State",
                    "Zip Code",
                ]
            )

            for contact in contacts:
                writer.writerow(contact.values())

        print(f"{len(contacts)} contacts exported to '{file_path}' successfully.")

    except Exception as e:
        print("Error exporting contacts:", e)

    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    ab_name = input("Enter Address Book Name to export contacts: ")
    export_contacts_to_csv(ab_name)
