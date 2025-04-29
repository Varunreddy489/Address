import json
from db_config import connect_db


def create_stored_procedure():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("DROP PROCEDURE IF EXISTS InsertContact")

    procedure_sql = """
    CREATE PROCEDURE InsertContact(
        IN p_address_book_id INT,
        IN p_first_name VARCHAR(50),
        IN p_last_name VARCHAR(50),
        IN p_email VARCHAR(100),
        IN p_phone_number VARCHAR(15),
        IN p_address VARCHAR(255),
        IN p_city VARCHAR(50),
        IN p_state VARCHAR(50),
        IN p_zip_code VARCHAR(10)
    )
    BEGIN
        INSERT INTO contacts (
            address_book_id, first_name, last_name,
            email, phone_number, address, city,
            state, zip_code
        ) VALUES (
            p_address_book_id, p_first_name, p_last_name,
            p_email, p_phone_number, p_address, p_city,
            p_state, p_zip_code
        );
    END
    """

    cursor.execute(procedure_sql)
    conn.commit()
    cursor.close()
    conn.close()
    print("Stored procedure created successfully.")


def seed_contacts_with_procedure(file_path="contacts.json", batch_size=100):
    conn = connect_db()
    cursor = conn.cursor()

    batch = []
    with open(file_path, "r") as f:
        for line_number, line in enumerate(f, 1):
            contact = json.loads(line.strip())
            values = (
                contact["address_book_id"],
                contact["first_name"],
                contact["last_name"],
                contact["email"],
                contact["phone_number"],
                contact["address"],
                contact["city"],
                contact["state"],
                contact["zip_code"],
            )
            batch.append(values)

            if len(batch) == batch_size:
                for row in batch:
                    cursor.callproc("InsertContact", row)
                conn.commit()
                print(f"Inserted batch ending at line {line_number}")
                batch.clear()

        if batch:
            for row in batch:
                cursor.callproc("InsertContact", row)
            conn.commit()
            print("Inserted final batch.")

    cursor.close()
    conn.close()
    print("Seeding complete.")


if __name__ == "__main__":
    create_stored_procedure()
    seed_contacts_with_procedure()
