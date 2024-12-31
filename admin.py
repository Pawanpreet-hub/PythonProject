from db import execute_query, fetch_all

def view_all_customers():
    query = "SELECT * FROM customers"
    customers = fetch_all(query)
    for customer in customers:
        print(f"ID: {customer[0]} | Username: {customer[1]} | Email: {customer[3]} | Phone: {customer[4]}")

def view_all_drivers():
    query = "SELECT * FROM drivers"
    drivers = fetch_all(query)
    for driver in drivers:
        print(f"ID: {driver[0]} | Username: {driver[1]} | Email: {driver[3]} | Phone: {driver[4]} | Availability: {driver[5]}")

def view_all_bookings():
    query = "SELECT * FROM bookings"
    bookings = fetch_all(query)
    for booking in bookings:
        print(f"Booking ID: {booking[0]} | Customer ID: {booking[1]} | Driver ID: {booking[2]} | Pickup: {booking[3]} | Dropoff: {booking[4]} | Status: {booking[5]}")
