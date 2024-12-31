import hashlib
from db import execute_query, fetch_one

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username, password, email, phone, table):
    existing_user = fetch_one(f"SELECT * FROM {table} WHERE username = %s", (username,))
    if existing_user:
        print(f"Username {username} already exists!")
        return False

    hashed_password = hash_password(password)
    query = f"INSERT INTO {table} (username, password, email, phone) VALUES (%s, %s, %s, %s)"
    execute_query(query, (username, hashed_password, email, phone))
    print(f"{table.capitalize()} registration successful!")
    return True

def login_user(username, password, table):
    hashed_password = hash_password(password)
    user = fetch_one(f"SELECT * FROM {table} WHERE username = %s AND password = %s", (username, hashed_password))
    if user:
        return user  # Return user data if login is successful
    else:
        print("Invalid username or password.")
        return None
