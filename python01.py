import tkinter as tk
from tkinter import ttk, messagebox
import re

# Fixed prices for bakery items
ITEMS = {
    "Bread": 3.0,
    "Garlic Bread": 4.5,
    "Chocolate Cake": 15.0,
    "Vanilla Cake": 12.0,
    "Chocolate Chip Cookies": 5.0,
    "Butter Cookies": 6.0,
    "Cheese Fart": 10.0,
    "Muffin Combo Pack (4 Pcs)": 20.0,
    "Assorted Donut Pack (6 Pcs)": 18.0,
}

DISCOUNT_MEMBER = 0.20  # 20% discount for members
DISCOUNT_NON_MEMBER = 0.10  # 10% discount for non-members

# Location options for the location dropdown
LOCATIONS = ["Main Branch", "Suburban Outlet", "Downtown Cafe", "Airport Kiosk"]


# --------------------------------------------
# Helper Functions
# --------------------------------------------

# Function to populate the dropdown with items
def update_item_combobox():
    items_with_prices = [f"{item} (RM {price:.2f})" for item, price in ITEMS.items()]
    item_combobox["values"] = items_with_prices
    item_combobox.set("Select Item")


# Function to extract the selected item and price
def parse_selected_item(selection):
    for item, price in ITEMS.items():
        if item in selection:
            return item, price
    return None, 0.0


# Function to calculate the discount
def calculate_discount(total, is_member):
    discount_rate = DISCOUNT_MEMBER if is_member else DISCOUNT_NON_MEMBER
    return total * discount_rate


# --------------------------------------------
# Validation Functions
# --------------------------------------------

def validate_name(name):
    if not name or not re.match("^[A-Za-z ]+$", name):
        messagebox.showerror("Validation Error", "Name must only contain letters and spaces.")
        return False
    return True


def validate_contact(contact):
    if not contact.isdigit() or not (10 <= len(contact) <= 15):
        messagebox.showerror("Validation Error", "Contact number must be between 10 and 15 digits.")
        return False
    return True


def validate_item(item):
    if item is None or item == "Select Item":
        messagebox.showerror("Validation Error", "Please select a valid item from the list.")
        return False
    return True


def validate_quantity(quantity):
    if not quantity.isdigit() or int(quantity) <= 0:
        messagebox.showerror("Validation Error", "Quantity must be a positive integer.")
        return False
    return True


# --------------------------------------------
# Submit Purchase Function
# --------------------------------------------

def submit_purchase():
    name = name_entry.get().strip()
    contact = contact_entry.get().strip()
    is_member = member_var.get()  # 1 for Member, 0 for Non-Member
    location = location_combobox.get()  # Selected location
    selection = item_combobox.get()
    item, price_per_item = parse_selected_item(selection)
    quantity = quantity_entry.get().strip()

    # Validate input fields
    if not validate_name(name) or not validate_contact(contact) or not validate_item(item) or not validate_quantity(quantity):
        return

    # Calculate total price and discount
    quantity = int(quantity)
    total_price = price_per_item * quantity
    discount = calculate_discount(total_price, is_member)
    final_price = total_price - discount

    # Display output
    membership_status = "Member" if is_member else "Non-Member"
    output_text.insert(
        tk.END,
        f"Customer Name: {name}\n"
        f"Contact: {contact}\n"
        f"Location: {location}\n"
        f"Membership: {membership_status}\n"
        f"Item: {item} @ RM {price_per_item:.2f}\n"
        f"Quantity: {quantity}\n"
        f"Total Price: RM {total_price:.2f}\n"
        f"Discount: RM {discount:.2f}\n"
        f"Final Price: RM {final_price:.2f}\n"
        + "-" * 40 + "\n"
    )
    clear_form()


# --------------------------------------------
# Clear Form Function
# --------------------------------------------

def clear_form():
    name_entry.delete(0, tk.END)
    contact_entry.delete(0, tk.END)
    member_var.set(0)  # Default to Non-Member
    item_combobox.set("Select Item")
    location_combobox.set("Select Location")  # Clear the location selection
    quantity_entry.delete(0, tk.END)


# --------------------------------------------
# GUI Setup
# --------------------------------------------

# Create the main application window
root = tk.Tk()
root.title("Bakery Purchase System")
root.geometry("800x900")
root.configure(bg="#e6f2ff")

# Title
title_label = tk.Label(root, text="BAKERY", font=("Arial", 28, "bold"), fg="#004080", bg="#e6f2ff")
title_label.place(x=300, y=10)

# Customer Name
name_label = tk.Label(root, text="Customer Name:", bg="#e6f2ff")
name_label.place(x=50, y=80)

name_entry = tk.Entry(root, width=40)
name_entry.place(x=200, y=80)

# Contact Number
contact_label = tk.Label(root, text="Contact Number:", bg="#e6f2ff")
contact_label.place(x=50, y=120)

contact_entry = tk.Entry(root, width=40)
contact_entry.place(x=200, y=120)

# Location Dropdown
location_label = tk.Label(root, text="Location:", bg="#e6f2ff")
location_label.place(x=50, y=160)

location_combobox = ttk.Combobox(root, state="readonly", width=40)
location_combobox.place(x=200, y=160)
location_combobox["values"] = LOCATIONS
location_combobox.set("Select Location")  # Default value

# Membership Radiobuttons
member_label = tk.Label(root, text="Membership:", bg="#e6f2ff")
member_label.place(x=50, y=200)

member_var = tk.IntVar(value=0)  # Default to Non-Member (0)
member_radio_member = tk.Radiobutton(root, text="Member", variable=member_var, value=1, bg="#e6f2ff")
member_radio_non_member = tk.Radiobutton(root, text="Non-Member", variable=member_var, value=0, bg="#e6f2ff")
member_radio_member.place(x=200, y=200)
member_radio_non_member.place(x=300, y=200)

# Item Selection
item_label = tk.Label(root, text="Item:", bg="#e6f2ff")
item_label.place(x=50, y=240)

item_combobox = ttk.Combobox(root, state="readonly", width=50)
item_combobox.place(x=200, y=240)
update_item_combobox()

# Quantity
quantity_label = tk.Label(root, text="Quantity:", bg="#e6f2ff")
quantity_label.place(x=50, y=280)

quantity_entry = tk.Entry(root, width=20)
quantity_entry.place(x=200, y=280)

# Buttons
submit_button = tk.Button(root, text="Submit", command=submit_purchase, bg="#0073e6", fg="white")
submit_button.place(x=200, y=320)

clear_button = tk.Button(root, text="Clear", command=clear_form, bg="#004080", fg="white")
clear_button.place(x=300, y=320)

# Output Text Box
output_label = tk.Label(root, text="Purchase Records:", bg="#e6f2ff")
output_label.place(x=50, y=380)

output_text = tk.Text(root, wrap=tk.WORD, width=90, height=20, bg="#cce6ff")
output_text.place(x=50, y=410)

# Run the application
root.mainloop()
