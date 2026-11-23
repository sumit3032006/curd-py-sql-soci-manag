import mysql.connector
from mysql.connector import Error

# Database configuration - edit these values as needed
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "*******"
DB_NAME = "society_db12"


def get_connection():
    """Return a MySQL connection object, or None on failure."""
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        return connection
    except Error as e:
        print("Database connection error:", e)
        return None
