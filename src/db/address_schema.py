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
                {"name": "phone", "type": "VARCHAR(15)"},
                {"name": "address", "type": "VARCHAR(255)"},
                {"name": "city", "type": "VARCHAR(50)"},
                {"name": "state", "type": "VARCHAR(50)"},
                {"name": "zip", "type": "VARCHAR(10)"},
            ],
            "foreign_keys": [
                "FOREIGN KEY (address_book_id) REFERENCES address_books(id) ON DELETE CASCADE"
            ],
        },
    }
