from db_config import connect_db


def create_contact_trigger():
    conn = connect_db()
    cursor = conn.cursor()

    try:
        cursor.execute("DROP TRIGGER IF EXISTS new_contact_trigger")

        trigger_sql = """
        CREATE TRIGGER new_contact_trigger
        AFTER INSERT ON contacts
        FOR EACH ROW
        INSERT INTO trigger_check (user_id, contact_name)
        VALUES (NEW.id, CONCAT(NEW.first_name, ' ', NEW.last_name));
        """

        cursor.execute(trigger_sql)
        conn.commit()
        print("Trigger created successfully.")

    except Exception as e:
        print("Error creating trigger:", e)

    finally:
        cursor.close()
        conn.close()


create_contact_trigger()
