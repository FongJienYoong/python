import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# Function to validate input fields to not to be empty
def validate_inputs(name, age, gender, height, weight):
    if not name:
        messagebox.showerror("Validation Error", "Name cannot be empty.")
        return False
    if not age.isdigit() or int(age) <= 0:
        messagebox.showerror("Validation Error", "Please enter a valid age.")
        return False
    if gender not in ["Male", "Female"]:
        messagebox.showerror("Validation Error", "Please select a gender.")
        return False
    if not height.isdigit() or int(height) <= 0:
        messagebox.showerror("Validation Error", "Please enter a valid height.")
        return False
    if not weight.isdigit() or int(weight) <= 0:
        messagebox.showerror("Validation Error", "Please enter a valid weight.")
        return False
    return True

# Function to calculate BMI
def calculate_bmi():
    name = name_entry.get().strip()
    age = age_entry.get().strip()
    gender = gender_var.get()
    height = height_entry.get().strip()
    weight = weight_entry.get().strip()

    # Validate inputs
    if not validate_inputs(name, age, gender, height, weight):
        return

    # Calculate BMI
    height_m = int(height) / 100  # Convert cm to meters
    bmi = int(weight) / (height_m ** 2)
    bmi = round(bmi, 2)

    # Show result in rich text box
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, f"BMI Calculation Result:\n")
    output_text.insert(tk.END, f"Name: {name}\n")
    output_text.insert(tk.END, f"Age: {age}\n")
    output_text.insert(tk.END, f"Gender: {gender}\n")
    output_text.insert(tk.END, f"Height: {height} cm\n")
    output_text.insert(tk.END, f"Weight: {weight} kg\n")
    output_text.insert(tk.END, f"BMI: {bmi}\n")

    # Determine BMI category
    if bmi < 18.5:
        output_text.insert(tk.END, "Category: Underweight\n")
    elif 18.5 <= bmi <= 24.9:
        output_text.insert(tk.END, "Category: Normal weight\n")
    elif 25 <= bmi <= 29.9:
        output_text.insert(tk.END, "Category: Overweight\n")
    else:
        output_text.insert(tk.END, "Category: Obesity\n")

# Function to clear the form
def clear_form():
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    weight_entry.delete(0, tk.END)
    gender_var.set("Male")
    output_text.delete(1.0, tk.END)

# Function to save the BMI result to database
def save_bmi_to_db():
    name = name_entry.get().strip()
    age = age_entry.get().strip()
    gender = gender_var.get()
    height = height_entry.get().strip()
    weight = weight_entry.get().strip()

    # Validate inputs
    if not validate_inputs(name, age, gender, height, weight):
        return

    try:
        # Connect to SQLite database
        conn = sqlite3.connect("bmi_calculator.db")
        cursor = conn.cursor()

        # Create table if not exists
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS bmi_results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                gender TEXT NOT NULL,
                height INTEGER NOT NULL,
                weight INTEGER NOT NULL,
                bmi REAL NOT NULL
            )
        """)

        # Calculate BMI
        height_m = int(height) / 100  # Convert cm to meters
        bmi = int(weight) / (height_m ** 2)

        # Insert data into table
        cursor.execute("INSERT INTO bmi_results (name, age, gender, height, weight, bmi) VALUES (?, ?, ?, ?, ?, ?)",
                       (name, int(age), gender, int(height), int(weight), bmi))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "BMI result saved successfully!")
    except Exception as e:
        messagebox.showerror("Database Error", f"An error occurred: {e}")

# Function to display saved results from database
def display_saved_bmi():
    output_text.delete(1.0, tk.END)
    try:
        conn = sqlite3.connect("bmi_calculator.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM bmi_results")
        rows = cursor.fetchall()
        for row in rows:
            record_id, name, age, gender, height, weight, bmi = row
            output_text.insert(tk.END, f"ID: {record_id}\n")
            output_text.insert(tk.END, f"Name: {name}\n")
            output_text.insert(tk.END, f"Age: {age}\n")
            output_text.insert(tk.END, f"Gender: {gender}\n")
            output_text.insert(tk.END, f"Height: {height} cm\n")
            output_text.insert(tk.END, f"Weight: {weight} kg\n")
            output_text.insert(tk.END, f"BMI: {bmi}\n")
            output_text.insert(tk.END, "-" * 40 + "\n")
        conn.close()
    except Exception as e:
        messagebox.showerror("Database Error", f"An error occurred: {e}")

# GUI Setup
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("600x700")

# Name
name_label = tk.Label(root, text="Name:")
name_label.place(x=20, y=20)
name_entry = tk.Entry(root)
name_entry.place(x=150, y=20, width=200)

# Age
age_label = tk.Label(root, text="Age:")
age_label.place(x=20, y=60)
age_entry = tk.Entry(root)
age_entry.place(x=150, y=60, width=200)

# Gender
gender_label = tk.Label(root, text="Gender:")
gender_label.place(x=20, y=100)
gender_var = tk.StringVar(value="Male")
male_radio = tk.Radiobutton(root, text="Male", variable=gender_var, value="Male")
male_radio.place(x=150, y=100)
female_radio = tk.Radiobutton(root, text="Female", variable=gender_var, value="Female")
female_radio.place(x=200, y=100)

# Height (cm)
height_label = tk.Label(root, text="Height (cm):")
height_label.place(x=20, y=140)
height_entry = tk.Entry(root)
height_entry.place(x=150, y=140, width=200)

# Weight (kg)
weight_label = tk.Label(root, text="Weight (kg):")
weight_label.place(x=20, y=180)
weight_entry = tk.Entry(root)
weight_entry.place(x=150, y=180, width=200)

# Submit Button
submit_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
submit_button.place(x=100, y=220)

# Save Button
save_button = tk.Button(root, text="Save Result", command=save_bmi_to_db)
save_button.place(x=200, y=220)

# Clear Button
clear_button = tk.Button(root, text="Clear", command=clear_form)
clear_button.place(x=300, y=220)

# Output Text Box
output_label = tk.Label(root, text="BMI Calculation Output:")
output_label.place(x=20, y=260)
output_text = tk.Text(root, wrap=tk.WORD, width=70, height=15)
output_text.place(x=20, y=290)

# Display Saved Results
display_button = tk.Button(root, text="Display Saved Results", command=display_saved_bmi)
display_button.place(x=100, y=570)

# Run the application
root.mainloop()
