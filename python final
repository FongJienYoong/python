import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# Prices for the cake
cake_price = {"bread": 3.0, "Cake": 4.0, "biscuit": 5.0}

# Create and connect to SQLite database
def create_database():
    conn = sqlite3.connect('bakery_sales.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS purchases
                      (customer_name TEXT, contact_number TEXT, item_name TEXT, quantity INTEGER, total_price REAL)''')
    conn.commit()
    conn.close()

# Function to insert purchase record into the database
def insert_record(name, contact, item, quantity, total):
    conn = sqlite3.connect('bakery_sales.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO purchases (customer_name, contact_number, item_name, quantity, total_price) VALUES (?, ?, ?, ?, ?)",
                   (name, contact, item, quantity, total))
    conn.commit()
    conn.close()

# Function to delete the last record from the database and the text box
def delete_last_record():
    conn = sqlite3.connect('bakery_sales.db')
    cursor = conn.cursor()

    # Get the last entry from the purchases table
    cursor.execute("SELECT rowid FROM purchases ORDER BY rowid DESC LIMIT 1")
    last_record = cursor.fetchone()

    if last_record:
        last_record_id = last_record[0]
        # Delete the last record from the database
        cursor.execute("DELETE FROM purchases WHERE rowid = ?", (last_record_id,))
        conn.commit()
        conn.close()

        # Remove the last record from the output text box
        txtoutput.config(state=tk.NORMAL)
        txtoutput.delete("1.0", tk.END)  # Clear the text box
        display_records()  # Refresh the records display
        txtoutput.config(state=tk.DISABLED)
    else:
        messagebox.showinfo("No Records", "No records to delete")

# Function to display all records from the database
def display_records():
    conn = sqlite3.connect('bakery_sales.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM purchases")
    records = cursor.fetchall()
    conn.close()

    # Clear the output text box and insert the records
    txtoutput.config(state=tk.NORMAL)  # Enable editing
    txtoutput.delete("1.0", tk.END)  # Clear the box

    if records:
        for record in records:
            txtoutput.insert(tk.END, f"Name: {record[0]}\n")
            txtoutput.insert(tk.END, f"Contact: {record[1]}\n")
            txtoutput.insert(tk.END, f"Item: {record[2]}\n")
            txtoutput.insert(tk.END, f"Quantity: {record[3]}\n")
            txtoutput.insert(tk.END, f"Total: {record[4]:.2f}\n")
            txtoutput.insert(tk.END, "-"*50 + "\n")
    else:
        txtoutput.insert(tk.END, "No records found.\n")
    
    txtoutput.config(state=tk.DISABLED)  # Re-disable editing

# Initialize the database
create_database()

# Create the main window
root = tk.Tk()
root.title("Fong Bakery")
root.geometry("600x700")

# lblname and txtname
lblname = tk.Label(root, text="Customer name : ")
lblname.place(x=20, y=20)

txtname = tk.Entry(root)
txtname.place(x=150, y=20, width=200)

# lblcontact and txtcontact
lblcontact = tk.Label(root, text="Contact number : ")
lblcontact.place(x=20, y=60)

txtcontact = tk.Entry(root)
txtcontact.place(x=150, y=60, width=200)

# lblselect and txtselect and add item
lblselect = tk.Label(root, text="Select your cake : ")
lblselect.place(x=20, y=100)

txtselect = ttk.Combobox(root)
txtselect.place(x=150, y=100, width=200)

txtselect['values'] = list(cake_price.keys())

# quantity
lblquantity = tk.Label(root, text="Quantity : ")
lblquantity.place(x=20, y=140)

txtquantity = tk.Entry(root)
txtquantity.place(x=150, y=140, width=200)

# submit button
btnsubmit = tk.Button(root, text="Submit")
btnsubmit.place(x=20, y=180)

# button clear
btnclear = tk.Button(root, text="Clear")
btnclear.place(x=100, y=180)

# output box
lbloutput = tk.Label(root, text="Purchase record")
lbloutput.place(x=20, y=220)

txtoutput = tk.Text(root, wrap=tk.WORD, width=70, height=15)
txtoutput.place(x=20, y=250)

# delete button
btndelete = tk.Button(root, text="Delete")
btndelete.place(x=20, y=510)

# Validation function
def submit():
    name = txtname.get()
    contact = txtcontact.get()
    selected_item = txtselect.get()
    quantity = txtquantity.get()

    # Validation for empty text boxes
    if not name:
        messagebox.showerror("Input Error", "Please fill in the name correctly")
        return
    if not contact:
        messagebox.showerror("Input Error", "Please fill in the contact correctly")
        return
    if not selected_item:
        messagebox.showerror("Input Error", "Please fill in the selected item correctly")
        return
    if not quantity:
        messagebox.showerror("Input Error", "Please fill in the quantity correctly")
        return
    
    # Validate the quantity to ensure it is a number
    try:
        quantity = int(quantity)
        if quantity <= 0:
            messagebox.showerror("Quantity Error", "Quantity must be a positive number")
            return
    except ValueError:
        messagebox.showerror("Quantity Error", "Quantity must be a valid number")
        return
    
    # Calculate the total price
    price = cake_price.get(selected_item, 0)
    total_price = price * quantity

    # Show details in the output box
    purchase_details = f"Name: {name}\nContact: {contact}\nItem: {selected_item}\nQuantity: {quantity}\nTotal: {total_price:.2f}\n"
    txtoutput.insert(tk.END, purchase_details + "-"*50 + "\n")

    # Insert the purchase record into the database
    insert_record(name, contact, selected_item, quantity, total_price)

    # Clear the fields after successful submission
    txtname.delete(0, tk.END)
    txtcontact.delete(0, tk.END)
    txtselect.set("")
    txtquantity.delete(0, tk.END)

def clear():
    # Clear the fields after successful submission
    txtname.delete(0, tk.END)
    txtcontact.delete(0, tk.END)
    txtselect.set("")
    txtquantity.delete(0, tk.END)
    txtoutput.delete("1.0", tk.END)

# Set the submit button with the submit function
btnsubmit.config(command=submit)

# Set the clear button with the clear function
btnclear.config(command=clear)

# Set the delete button with the delete function
btndelete.config(command=delete_last_record)

# Show All Records Button
btnshow = tk.Button(root, text="Show All Records", command=display_records)
btnshow.place(x=100, y=510)

# Run the application
root.mainloop()
