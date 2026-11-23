from config.db import get_connection
from mysql.connector import Error


def add_member(member_name, flat_number, phone, monthly_maintenance, payment_status):
    """Insert a new member. Return True on success, False on failure."""
    connection = None
    cursor = None
    try:
        connection = get_connection()
        if connection is None:
            return False
        cursor = connection.cursor()
        query = (
            "INSERT INTO society_members "
            "(member_name, flat_number, phone, monthly_maintenance, payment_status) "
            "VALUES (%s, %s, %s, %s, %s)"
        )
        cursor.execute(query, (member_name, flat_number, phone, monthly_maintenance, payment_status))
        connection.commit()
        return True
    except Error as e:
        print("Error adding member:", e)
        if connection:
            connection.rollback()
        return False
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


def get_all_members():
    """Fetch all members. Return list of records."""
    connection = None
    cursor = None
    try:
        connection = get_connection()
        if connection is None:
            return []
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM society_members")
        records = cursor.fetchall()
        return records
    except Error as e:
        print("Error fetching members:", e)
        return []
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


def get_member_by_id(member_id):
    """Fetch a single member by ID. Return record or None."""
    connection = None
    cursor = None
    try:
        connection = get_connection()
        if connection is None:
            return None
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM society_members WHERE member_id = %s", (member_id,))
        record = cursor.fetchone()
        return record
    except Error as e:
        print("Error fetching member:", e)
        return None
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


def update_member(member_id, member_name, flat_number, phone, monthly_maintenance, payment_status):
    """Update an existing member. Return True on success, False on failure."""
    connection = None
    cursor = None
    try:
        connection = get_connection()
        if connection is None:
            return False
        cursor = connection.cursor()
        query = (
            "UPDATE society_members SET member_name=%s, flat_number=%s, phone=%s, "
            "monthly_maintenance=%s, payment_status=%s WHERE member_id=%s"
        )
        cursor.execute(query, (member_name, flat_number, phone, monthly_maintenance, payment_status, member_id))
        connection.commit()
        if cursor.rowcount == 0:
            print("Member not found.")
            return False
        return True
    except Error as e:
        print("Error updating member:", e)
        if connection:
            connection.rollback()
        return False
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


def delete_member(member_id):
    """Delete a member by ID. Return True on success, False on failure."""
    connection = None
    cursor = None
    try:
        connection = get_connection()
        if connection is None:
            return False
        cursor = connection.cursor()
        cursor.execute("DELETE FROM society_members WHERE member_id = %s", (member_id,))
        connection.commit()
        if cursor.rowcount == 0:
            print("Member not found.")
            return False
        return True
    except Error as e:
        print("Error deleting member:", e)
        if connection:
            connection.rollback()
        return False
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


def search_member(member_name):
    """Search members by partial name. Return list of records."""
    connection = None
    cursor = None
    try:
        connection = get_connection()
        if connection is None:
            return []
        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM society_members WHERE member_name LIKE %s",
            ("%" + member_name + "%",)
        )
        records = cursor.fetchall()
        return records
    except Error as e:
        print("Error searching members:", e)
        return []
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
