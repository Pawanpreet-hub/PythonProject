from tkinter import mainloop

import mysql.connector
from mysql.connector import Error
from datetime import datetime
import bcrypt


# Function to establish MySQL connection
def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',  # MySQL server address
            database='test',  # Database name
            user='root',  # MySQL username
            password='Dhaliwal2005'  # MySQL password
        )
        if connection.is_connected():
            print("Successfully connected to MySQL")
        return connection
    except Error as e:
        print(f"Error: {e}")
        return None


# Function to hash password before storing in the database
def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


# Function to verify password during login
def verify_password(stored_hash, password):
    return bcrypt.checkpw(password.encode('utf-8'), stored_hash)


# Function to register a new customer
def register_customer(name, email, phone, password):
    connection = create_connection()
    cursor = connection.cursor()

    hashed_password = hash_password(password)
    query = "INSERT INTO customers (name, email, password) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, email, hashed_password))

    connection.commit()
    print("Registration successful!")

    cursor.close()
    connection.close()


# Function for customer login
def login(email, password):
    connection = create_connection()
    cursor = connection.cursor()

    query = "SELECT * FROM customers WHERE email = %s"
    cursor.execute(query, (email,))
    customer = cursor.fetchone()

    cursor.close()
    connection.close()

    if customer and verify_password(customer[3], password):
        return customer[0]  # Return customer_id on successful login
    else:
        return None  # Invalid login


# Function to view all bookings of a customer
def view_bookings(customer_id):
    connection = create_connection()
    cursor = connection.cursor()

    query = "SELECT * FROM bookings WHERE customer_id = %s AND status = 'booked'"
    cursor.execute(query, (customer_id,))
    bookings = cursor.fetchall()

    if bookings:
        print(f"Bookings for customer ID {customer_id}:")
        for booking in bookings:
            print(f"Booking ID: {booking[0]}, Pickup: {booking[2]}, Dropoff: {booking[3]}, Time: {booking[4]}")
    else:
        print("No bookings found.")

    cursor.close()
    connection.close()


# Function to make a new booking for a customer
def make_booking(customer_id, pickup_location, dropoff_location):
    connection = create_connection()
    cursor = connection.cursor()

    booking_time = datetime.now()
    query = "INSERT INTO bookings (customer_id, pickup_location, dropoff_location, booking_time) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (customer_id, pickup_location, dropoff_location, booking_time))

    connection.commit()
    print("Booking successful!")

    cursor.close()
    connection.close()


# Function to cancel a booking
def cancel_booking(booking_id):
    connection = create_connection()
    cursor = connection.cursor()

    query = "UPDATE bookings SET status = 'cancelled' WHERE booking_id = %s"
    cursor.execute(query, (booking_id,))

    connection.commit()
    print(f"Booking with ID {booking_id} has been cancelled.")

    cursor.close()
    connection.close()


# Main program loop
def main():
    print("Welcome to the Taxi Booking System!")

    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            register_customer(name, email, password)
        elif choice == '2':
            email = input("Enter your email: ")
            password = input("Enter your password: ")

            customer_id = login(email, password)
            if customer_id:
                print(f"Welcome back, customer {customer_id}!")

                while True:
                    print("\n1. View My Bookings")
                    print("2. Make a Booking")
                    print("3. Cancel a Booking")
                    print("4. Logout")

                    user_choice = input("Enter your choice: ")

                    if user_choice == '1':
                        view_bookings(customer_id)
                    elif user_choice == '2':
                        pickup_location = input("Enter pickup location: ")
                        dropoff_location = input("Enter dropoff location: ")
                        make_booking(customer_id, pickup_location, dropoff_location)
                    elif user_choice == '3':
                        booking_id = int(input("Enter booking ID to cancel: "))
                        cancel_booking(booking_id)
                    elif user_choice == '4':
                        print("Logging out...")
                        break
                    else:
                        print("Invalid choice. Please try again.")
            else:
                print("Invalid login credentials. Please try again.")
        elif choice == '3':
            print("Exiting system...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    mainloop()
