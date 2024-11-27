import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Fixed prices for flight destinations and classes
DESTINATION_PRICES = {
    "New York": 500.0,
    "London": 600.0,
    "Paris": 550.0,
    "Tokyo": 650.0,
    "Sydney": 700.0
}

CLASS_PRICES = {
    "Economy": 0.0,
    "Business": 200.0,
    "First Class": 500.0
}

# Function to calculate total price
def calculate_total_price():
    try:
        # Get selected destination, class and number of passengers
        destination = destination_combobox.get()
        flight_class = class_var.get()
        num_passengers = int(passenger_entry.get())

        if num_passengers <= 0:
            messagebox.showerror("Input Error", "Number of passengers must be greater than zero.")
            return

        # Get base price for the destination
        base_price = DESTINATION_PRICES.get(destination, 0.0)

        # Get additional cost for the class
        class_price = CLASS_PRICES.get(flight_class, 0.0)

        # Calculate total price (base price + class price) * number of passengers
        total_price = (base_price + class_price) * num_passengers

        # Display the total price in the output box
        output_text.delete(1.0, tk.END)  # Clear previous output
        output_text.insert(tk.END, f"Name: {name_entry.get()}\n")
        output_text.insert(tk.END, f"Contact: {contact_entry.get()}\n")
        output_text.insert(tk.END, f"Destination: {destination}\n")
        output_text.insert(tk.END, f"Flight Class: {flight_class}\n")
        output_text.insert(tk.END, f"Number of Passengers: {num_passengers}\n")
        output_text.insert(tk.END, f"Total Price: ${total_price:.2f}\n")
        messagebox.showinfo("Booking Confirmation", f"Your booking is confirmed! Total price: ${total_price:.2f}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number for passengers.")

# Function to clear the form
def clear_form():
    name_entry.delete(0, tk.END)
    contact_entry.delete(0, tk.END)
    destination_combobox.set("Select Destination")
    class_var.set("Economy")
    passenger_entry.delete(0, tk.END)
    output_text.delete(1.0, tk.END)

# GUI Setup
root = tk.Tk()
root.title("Flight Booking System")
root.geometry("600x600")

# Title
title_label = tk.Label(root, text="Flight Booking System", font=("Helvetica", 16, "bold"))
title_label.place(x=180, y=10)

# Name Label and Entry
name_label = tk.Label(root, text="Enter your name:")
name_label.place(x=20, y=60)
name_entry = tk.Entry(root)
name_entry.place(x=180, y=60, width=200)

# Contact Label and Entry
contact_label = tk.Label(root, text="Enter your contact number:")
contact_label.place(x=20, y=100)
contact_entry = tk.Entry(root)
contact_entry.place(x=180, y=100, width=200)

# Number of Passengers Label and Entry
passenger_label = tk.Label(root, text="Enter number of passengers:")
passenger_label.place(x=20, y=140)
passenger_entry = tk.Entry(root)
passenger_entry.place(x=180, y=140, width=200)

# Destination Selection (Dropdown)
destination_label = tk.Label(root, text="Select Destination:")
destination_label.place(x=20, y=180)
destination_combobox = ttk.Combobox(root, values=list(DESTINATION_PRICES.keys()))
destination_combobox.place(x=180, y=180, width=200)
destination_combobox.set("Select Destination")

# Flight Class Selection (Radio Buttons)
class_label = tk.Label(root, text="Select Flight Class:")
class_label.place(x=20, y=220)
class_var = tk.StringVar(value="Economy")
economy_radio = tk.Radiobutton(root, text="Economy", variable=class_var, value="Economy")
economy_radio.place(x=180, y=220)
business_radio = tk.Radiobutton(root, text="Business", variable=class_var, value="Business")
business_radio.place(x=260, y=220)
first_class_radio = tk.Radiobutton(root, text="First Class", variable=class_var, value="First Class")
first_class_radio.place(x=340, y=220)

# Calculate Button
calculate_button = tk.Button(root, text="Calculate Total", command=calculate_total_price)
calculate_button.place(x=150, y=260)

# Clear Button
clear_button = tk.Button(root, text="Clear", command=clear_form)
clear_button.place(x=250, y=260)

# Output Text Box
output_label = tk.Label(root, text="Booking Details:")
output_label.place(x=20, y=300)
output_text = tk.Text(root, wrap=tk.WORD, width=60, height=10)
output_text.place(x=20, y=330)

# Run the application
root.mainloop()
