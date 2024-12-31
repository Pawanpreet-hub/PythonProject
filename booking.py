from db import execute_query, fetch_all

def create_booking(customer_id, pickup_location, dropoff_location):
    query = """INSERT INTO bookings (customer_id, pickup_location, dropoff_location, booking_time)
               VALUES (%s, %s, %s, NOW())"""
    execute_query(query, (customer_id, pickup_location, dropoff_location))
    print("Booking created successfully!")

def view_bookings(customer_id):
    query = "SELECT * FROM bookings WHERE customer_id = %s"
    bookings = fetch_all(query, (customer_id,))
    if bookings:
        for booking in bookings:
            print(f"Booking ID: {booking[0]} | Pickup: {booking[2]} | Dropoff: {booking[3]} | Status: {booking[5]}")
    else:
        print("No bookings found.")

def cancel_booking(booking_id):
    query = "UPDATE bookings SET status = 'Cancelled' WHERE booking_id = %s"
    execute_query(query, (booking_id,))
    print(f"Booking {booking_id} has been cancelled.")

def view_pending_bookings(driver_id):
    query = "SELECT * FROM bookings WHERE driver_id IS NULL AND status = 'Pending'"
    bookings = fetch_all(query)
    if bookings:
        for booking in bookings:
            print(f"Booking ID: {booking[0]} | Pickup: {booking[2]} | Dropoff: {booking[3]} | Status: {booking[5]}")
    else:
        print("No pending bookings.")

def accept_booking(booking_id, driver_id):
    query = "UPDATE bookings SET status = 'Accepted', driver_id = %s WHERE booking_id = %s"
    execute_query(query, (driver_id, booking_id))
    print(f"Booking {booking_id} has been accepted.")

def reject_booking(booking_id):
    query = "UPDATE bookings SET status = 'Rejected' WHERE booking_id = %s"
    execute_query(query, (booking_id,))
    print(f"Booking {booking_id} has been rejected.")
