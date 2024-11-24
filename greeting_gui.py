import tkinter as tk
from tkinter import messagebox
import time

def get_greeting(hour):
    if 0 <= hour < 12:
        return "Good Morning Sir!"
    elif 12 <= hour < 17:
        return "Good Afternoon Sir!"
    elif 17 <= hour < 24:
        return "Good Night Sir!"
    else:
        return "Invalid Time!"

def display_greeting():
    try:
        hour = int(hour_entry.get())
        minutes = int(minutes_entry.get())
        seconds = int(seconds_entry.get())

        if (0 <= hour < 24) and (0 <= minutes < 60) and (0 <= seconds < 60):
            greeting = get_greeting(hour)
            messagebox.showinfo("Greeting", greeting)
        else:
            messagebox.showerror("Invalid Input", "Please enter valid time values.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid integers for time.")

# Create the main window
root = tk.Tk()
root.title("Greeting Based on Time")

# Create and place the labels and entries for hour, minutes, and seconds
tk.Label(root, text="Enter Hour:").grid(row=0, column=0, padx=10, pady=10)
hour_entry = tk.Entry(root)
hour_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Enter Minutes:").grid(row=1, column=0, padx=10, pady=10)
minutes_entry = tk.Entry(root)
minutes_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Enter Seconds:").grid(row=2, column=0, padx=10, pady=10)
seconds_entry = tk.Entry(root)
seconds_entry.grid(row=2, column=1, padx=10, pady=10)

# Create and place the button to display the greeting
greet_button = tk.Button(root, text="Get Greeting", command=display_greeting)
greet_button.grid(row=3, columnspan=2, padx=10, pady=10)

# Run the application
root.mainloop()
