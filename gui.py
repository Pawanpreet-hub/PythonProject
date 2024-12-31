import tkinter as tk
from tkinter import messagebox
from user import register_user, login_user
from booking import create_booking, view_bookings, cancel_booking, view_pending_bookings, accept_booking, reject_booking
from admin import view_all_customers, view_all_drivers, view_all_bookings

class TaxiBookingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Taxi Booking System")
        self.logged_in_user = None
        self.user_type = None  # 'customer', 'driver', or 'admin'
        self.create_widgets()

    def create_widgets(self):
        self.login_frame = tk.Frame(self.root)
        self.login_frame.pack()

        tk.Label(self.login_frame, text="Username:").grid(row=0, column=0)
        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.grid(row=0, column=1)

        tk.Label(self.login_frame, text="Password:").grid(row=1, column=0)
        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.password_entry.grid(row=1, column=1)

        self.user_type_var = tk.StringVar()
        self.user_type_var.set("customer")  # Default to 'customer'
        tk.Radiobutton(self.login_frame, text="Customer", variable=self.user_type_var, value="customer").grid(row=2, column=0)
        tk.Radiobutton(self.login_frame, text="Driver", variable=self.user_type_var, value="driver").grid(row=2, column=1)
        tk.Radiobutton(self.login_frame, text="Admin", variable=self.user_type_var, value="admin").grid(row=2, column=2)

        self.login_button = tk.Button(self.login_frame, text="Login", command=self.login)
        self.login_button.grid(row=3, columnspan=3)

        self.register_button = tk.Button(self.login_frame, text="Register", command=self.register)
        self.register_button.grid(row=4, columnspan=3)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        self.user_type = self.user_type_var.get()

        if self.user_type == "customer":
            user = login_user(username, password, "customers")
        elif self.user_type == "driver":
            user = login_user(username, password, "drivers")
        else:
            user = login_user(username, password, "admins")

        if user:
            self.logged_in_user = user
            messagebox.showinfo("Login", "Login successful!")
            self.show_user_dashboard()
        else:
            messagebox.showerror("Login", "Invalid credentials.")

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        email = "test@example.com"  # Hardcoded for simplicity
        phone = "1234567890"  # Hardcoded for simplicity

        if self.user_type == "customer":
            if register_user(username, password, email,  "customers"):
                self.logged_in_user = (None,)  # Replace with actual user data after registration
                self.show_user_dashboard()
        elif self.user_type == "driver":
            if register_user(username, password, email,  "drivers"):
                self.logged_in_user = (None,)  # Replace with actual user data after registration
                self.show_user_dashboard()
        else:
            if register_user(username, password, email, phone, "admins"):
                self.logged_in_user = (None,)  # Replace with actual user data after registration
                self.show_user_dashboard()

    def show_user_dashboard(self):
        self.login_frame.pack_forget()

        if self.user_type == "customer":
            self.customer_dashboard()
        elif self.user_type == "driver":
            self.driver_dashboard()
        else:
            self.admin_dashboard()

    def customer_dashboard(self):
        self.booking_frame = tk.Frame(self.root)
        self.booking_frame.pack()

        self.make_booking_button = tk.Button(self.booking_frame, text="Make a Booking", command=self.make_booking)
        self.make_booking_button.pack()

        self.view_bookings_button = tk.Button(self.booking_frame, text="View Bookings", command=self.view_bookings)
        self.view_bookings_button.pack()

        self.cancel_booking_button = tk.Button(self.booking_frame, text="Cancel Booking", command=self.cancel_booking)
        self.cancel_booking_button.pack()

    def make_booking(self):
        pickup = "Location A"  # Replace with actual user input
        dropoff = "Location B"  # Replace with actual user input
        create_booking(self.logged_in_user[0], pickup, dropoff)
        messagebox.showinfo("Booking", "Your booking has been made!")

    def view_bookings(self):
        view_bookings(self.logged_in_user[0])

    def cancel_booking(self):
        booking_id = 1  # Example, replace with dynamic selection
        cancel_booking(booking_id)

    def driver_dashboard(self):
        self.driver_frame = tk.Frame(self.root)
        self.driver_frame.pack()

        self.view_pending_button = tk.Button(self.driver_frame, text="View Pending Bookings", command=self.view_pending)
        self.view_pending_button.pack()

        self.accept_button = tk.Button(self.driver_frame, text="Accept Booking", command=self.accept_booking)
        self.accept_button.pack()

        self.reject_button = tk.Button(self.driver_frame, text="Reject Booking", command=self.reject_booking)
        self.reject_button.pack()

    def view_pending(self):
        view_pending_bookings(self.logged_in_user[0])

    def accept_booking(self):
        booking_id = 1  # Example, replace with dynamic selection
        accept_booking(booking_id, self.logged_in_user[0])

    def reject_booking(self):
        booking_id = 1  # Example, replace with dynamic selection
        reject_booking(booking_id)

    def admin_dashboard(self):
        self.admin_frame = tk.Frame(self.root)
        self.admin_frame.pack()

        self.view_customers_button = tk.Button(self.admin_frame, text="View Customers", command=self.view_customers)
        self.view_customers_button.pack()

        self.view_drivers_button = tk.Button(self.admin_frame, text="View Drivers", command=self.view_drivers)
        self.view_drivers_button.pack()

        self.view_bookings_button = tk.Button(self.admin_frame, text="View Bookings", command=self.view_bookings)
        self.view_bookings_button.pack()

    def view_customers(self):
        view_all_customers()

    def view_drivers(self):
        view_all_drivers()

    def view_bookings(self):
        view_all_bookings()


if __name__ == "__main__":
    root = tk.Tk()
    app = TaxiBookingApp(root)
    root.mainloop()









