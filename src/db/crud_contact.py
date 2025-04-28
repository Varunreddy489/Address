from __future__ import annotations
from db_config import connect
from mysql.connector import Error
from address_schema import TableSchema
from typing import List, Optional
from schema.schema import ContactSchema


def _ensure_schema(cur) -> None:
    print("Creating Tables with Queries:\n")
    for table_key in TableSchema.table_schema.keys():
        query = TableSchema.get_create_statement(table_key)
        print(f"{TableSchema.get_table_name(table_key)}:\n{query}\n")
        cur.execute(query)


def create_address_book(name: str) -> Optional[int]:
    with connect() as conn:
        if conn is None:
            return None
        cur = conn.cursor()
        _ensure_schema(cur)
        try:
            cur.execute("INSERT IGNORE INTO address_books (name) VALUES (%s)", (name,))
            conn.commit()
            cur.execute("SELECT id FROM address_books WHERE name=%s", (name,))
            result = cur.fetchone()
            if result:
                (ab_id,) = result
                return ab_id
            return None
        except Error as e:
            print("DB error:", e)
            return None
        finally:
            cur.close()


def list_address_books() -> List[tuple[int, str]]:
    with connect() as conn:
        if conn is None:
            return []
        cur = conn.cursor()
        _ensure_schema(cur)
        cur.execute("SELECT id, name FROM address_books ORDER BY name")
        rows = cur.fetchall()
        cur.close()
        return rows


def add_contact(book_id: int, detail: ContactSchema) -> None:
    with connect() as conn:
        if conn is None:
            return
        cur = conn.cursor()
        _ensure_schema(cur)
        cols = (
            "address_book_id, first_name, last_name, email, phone, "
            "address, city, state, zip"
        )
        vals = (
            book_id,
            detail.first_name,
            detail.last_name,
            detail.email,
            detail.phone,
            detail.address,
            detail.city,
            detail.state,
            detail.zip_code,
        )
        query = (
            f"INSERT INTO contacts ({cols}) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        )
        cur.execute(query, vals)
        conn.commit()
        cur.close()


def fetch_contacts(book_id: int) -> List[ContactSchema]:
    with connect() as conn:
        if conn is None:
            return []
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT * FROM contacts WHERE address_book_id=%s", (book_id,))
        rows = cur.fetchall()
        cur.close()
    return [
        ContactSchema(
            first_name=row["first_name"],
            last_name=row["last_name"],
            address=row["address"],
            city=row["city"],
            state=row["state"],
            zip_code=row["zip"],
            phone=row["phone"],
            email=row["email"],
        )
        for row in rows
    ]


def update_contact(book_id: int, old: ContactSchema, new: ContactSchema) -> None:
    with connect() as conn:
        if conn is None:
            return
        cur = conn.cursor()
        query = """
            UPDATE contacts
            SET first_name=%s, last_name=%s, email=%s, phone=%s,
                address=%s, city=%s, state=%s, zip=%s
            WHERE address_book_id=%s AND first_name=%s AND last_name=%s
        """
        values = (
            new.first_name,
            new.last_name,
            new.email,
            new.phone,
            new.address,
            new.city,
            new.state,
            new.zip_code,
            book_id,
            old.first_name,
            old.last_name,
        )
        cur.execute(query, values)
        conn.commit()
        cur.close()


def delete_contact_db(book_id: int, detail: ContactSchema) -> None:
    with connect() as conn:
        if conn is None:
            return
        cur = conn.cursor()
        query = """
            DELETE FROM contacts
            WHERE address_book_id=%s AND first_name=%s AND last_name=%s
        """
        cur.execute(query, (book_id, detail.first_name, detail.last_name))
        conn.commit()
        cur.close()
