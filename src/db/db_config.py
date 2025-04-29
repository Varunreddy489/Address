import mysql.connector


def connect_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Varunreddy@123",
            database="Address_Book_Db",
        )
        if conn.is_connected():
            print("Successfully connected to the database")
            return conn
        else:
            return None
    except mysql.connector.Error as err:
        print(f"Connection error: {err}")
        return None
