import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",       # Change if you're using a different host
            user="root",            # MySQL user
            password="Dhaliwal2005",            # MySQL password
            database="test"
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

def execute_query(query, values=None):
    connection = create_connection()
    cursor = connection.cursor()
    try:
        if values:
            cursor.execute(query, values)
        else:
            cursor.execute(query)
        connection.commit()
    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        connection.close()

def fetch_one(query, values=None):
    connection = create_connection()
    cursor = connection.cursor()
    try:
        if values:
            cursor.execute(query, values)
        else:
            cursor.execute(query)
        result = cursor.fetchone()
        return result
    except Error as e:
        print(f"Error: {e}")
        return None
    finally:
        cursor.close()
        connection.close()

def fetch_all(query, values=None):
    connection = create_connection()
    cursor = connection.cursor()
    try:
        if values:
            cursor.execute(query, values)
        else:
            cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"Error: {e}")
        return []
    finally:
        cursor.close()
        connection.close()
