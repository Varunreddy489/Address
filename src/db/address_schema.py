import mysql.connector
from db_config import connect_db


class TableSchema:
    table_schema = {
        "addressbook": {
            "table_name": "address_books",
            "columns": [
                {
                    "name": "id",
                    "type": "INT",
                    "constraint": ["AUTO_INCREMENT", "PRIMARY KEY"],
                },
                {
                    "name": "name",
                    "type": "VARCHAR(100)",
                    "constraint": ["UNIQUE", "NOT NULL"],
                },
            ],
        },
        "contacts": {
            "table_name": "contacts",
            "columns": [
                {
                    "name": "id",
                    "type": "INT",
                    "constraint": ["AUTO_INCREMENT", "PRIMARY KEY"],
                },
                {"name": "address_book_id", "type": "INT", "constraint": ["NOT NULL"]},
                {"name": "first_name", "type": "VARCHAR(50)"},
                {"name": "last_name", "type": "VARCHAR(50)"},
                {"name": "email", "type": "VARCHAR(100)"},
                {"name": "phone_number", "type": "VARCHAR(15)"},
                {"name": "address", "type": "VARCHAR(255)"},
                {"name": "city", "type": "VARCHAR(50)"},
                {"name": "state", "type": "VARCHAR(50)"},
                {"name": "zip_code", "type": "VARCHAR(10)"},
            ],
            "foreign_keys": [
                "FOREIGN KEY (address_book_id) REFERENCES address_books(id) ON DELETE CASCADE"
            ],
        },
        "trigger_check": {
            "table_name": "trigger_check",
            "columns": [
                {
                    "name": "id",
                    "type": "INT",
                    "constraint": ["AUTO_INCREMENT", "PRIMARY KEY"],
                },
                {
                    "name": "user_id",
                    "type": "INT",
                },
                {
                    "name": "contact_name",
                    "type": "VARCHAR(100)",
                },
            ],
            "foreign_keys": [
                "FOREIGN KEY (user_id) REFERENCES contacts(id) ON DELETE CASCADE"
            ],
        },
    }

    @classmethod
    def get_create_statement(cls, table_key: str) -> str:
        if table_key not in cls.table_schema:
            raise ValueError(f"Table schema for {table_key} not found.")

        schema = cls.table_schema[table_key]
        lines = []

        for col in schema["columns"]:
            column_str = f"{col['name']} {col['type']}"
            if "constraint" in col:
                constraint_str = " ".join(col["constraint"])
                column_str = f"{column_str} {constraint_str}"
            lines.append(column_str.strip())

        if "foreign_keys" in schema:
            lines.extend(schema["foreign_keys"])

        body = ",\n    ".join(lines)

        return f"CREATE TABLE IF NOT EXISTS {schema['table_name']} (\n{body}\n);"


def create_tables():
    connection = None
    cursor = None
    try:
        connection = connect_db()
        if connection is None or isinstance(connection, tuple):
            raise Exception(
                "Failed to connect to the database or invalid connection object returned."
            )

        cursor = connection.cursor()

        addressbook_create_sql = TableSchema.get_create_statement("addressbook")
        print("Creating address_books table with:")
        print(addressbook_create_sql)

        cursor.execute(addressbook_create_sql)
        print("Address book table created successfully!")

        contacts_create_sql = TableSchema.get_create_statement("contacts")
        print("\nCreating contacts table with:")
        print(contacts_create_sql)

        cursor.execute(contacts_create_sql)
        print("Contacts table created successfully!")

        trigger_check_create_sql = TableSchema.get_create_statement("trigger_check")
        print("\nCreating Trigger check table with:")
        print(trigger_check_create_sql)

        cursor.execute(trigger_check_create_sql)
        print("Trigger check created successfully!")

        connection.commit()

    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        if connection:
            connection.rollback()

    except Exception as err:
        print(f"Error: {err}")

    finally:
        if cursor:
            cursor.close()
        if (
            connection
            and hasattr(connection, "is_connected")
            and connection.is_connected()
        ):
            connection.close()
            print("Database connection closed.")


create_tables()
