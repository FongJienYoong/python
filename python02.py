import tkinter as tk
from tkinter import messagebox

# Function to calculate BMI and determine status
def calculate_bmi():
    try:
        # Get user input values for weight, height, age, and gender
        name = name_entry.get().strip()
        age = age_entry.get().strip()
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        # Validate inputs
        if not name or not age or weight <= 0 or height <= 0:
            messagebox.showerror("Input Error", "Please fill in all fields with valid data.")
            return

        # Calculate BMI
        bmi = weight / (height ** 2)

        # Determine BMI status
        if bmi < 18.5:
            status = "Underweight"
        elif 18.5 <= bmi < 24.9:
            status = "Normal weight"
        elif 25 <= bmi < 29.9:
            status = "Overweight"
        else:
            status = "Obese"

        # Get gender
        gender = gender_var.get()
        
        # Display the result in the rich text box
        output_text.delete(1.0, tk.END)  # Clear previous output
        output_text.insert(tk.END, f"Name: {name}\n")
        output_text.insert(tk.END, f"Age: {age}\n")
        output_text.insert(tk.END, f"Gender: {gender}\n")
        output_text.insert(tk.END, f"Your BMI is: {bmi:.2f}\n")
        output_text.insert(tk.END, f"Status: {status}\n")
    
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for weight and height.")

# Clear Form Function
def clear_form():
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    gender_var.set("Male")
    output_text.delete(1.0, tk.END)

# GUI Setup
root = tk.Tk()
root.title("BMI Calculator")  # Title for the application
root.geometry("500x650")

# Title Label
title_label = tk.Label(root, text="BMI Calculator", font=("Helvetica", 16, "bold"))
title_label.place(x=150, y=10)

# Name Label and Entry
name_label = tk.Label(root, text="Enter your name:")
name_label.place(x=20, y=60)
name_entry = tk.Entry(root)
name_entry.place(x=180, y=60, width=200)

# Age Label and Entry
age_label = tk.Label(root, text="Enter your age:")
age_label.place(x=20, y=100)
age_entry = tk.Entry(root)
age_entry.place(x=180, y=100, width=200)

# Weight Label and Entry
weight_label = tk.Label(root, text="Enter your weight (kg):")
weight_label.place(x=20, y=140)
weight_entry = tk.Entry(root)
weight_entry.place(x=180, y=140, width=200)

# Height Label and Entry
height_label = tk.Label(root, text="Enter your height (m):")
height_label.place(x=20, y=180)
height_entry = tk.Entry(root)
height_entry.place(x=180, y=180, width=200)

# Gender Radio Buttons
gender_label = tk.Label(root, text="Select Gender:")
gender_label.place(x=20, y=220)
gender_var = tk.StringVar(value="Male")
gender_radio1 = tk.Radiobutton(root, text="Male", variable=gender_var, value="Male")
gender_radio1.place(x=180, y=220)
gender_radio2 = tk.Radiobutton(root, text="Female", variable=gender_var, value="Female")
gender_radio2.place(x=260, y=220)

# Calculate BMI Button
calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.place(x=150, y=260)

# Clear Form Button
clear_button = tk.Button(root, text="Clear", command=clear_form)
clear_button.place(x=230, y=260)

# Output Rich Text Box
output_label = tk.Label(root, text="BMI Calculation Result:")
output_label.place(x=20, y=300)
output_text = tk.Text(root, wrap=tk.WORD, width=40, height=10)
output_text.place(x=20, y=330)

# Run the application
root.mainloop()
