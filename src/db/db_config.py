import mysql.connector
from mysql.connector import Error


def connect_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Varunreddy@123",
            database="Address_Book_Db",
        )
        return connection
    except mysql.connector.Error as err:
        print(f" Error: {err}")
        return None