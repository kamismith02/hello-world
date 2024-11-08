import tkinter as tk
import time

# Function to display "Hello, World!" after the countdown
def show_hello_world():
    countdown_label.config(text="Hello, World!", fg="hot pink", font=("Arial", 30))

# Function to update the countdown
def countdown(count):
    if count > 0:
        countdown_label.config(text=str(count), font=("Arial", 40))
        root.after(1000, countdown, count - 1)  # Countdown by 1 each second
    else:
        show_hello_world()

# Create the main Tkinter window
root = tk.Tk()
root.title("Hello World Countdown")
root.geometry("300x200")

# Create a label for displaying the countdown and "Hello, World!"
countdown_label = tk.Label(root, text="", font=("Arial", 40))
countdown_label.pack(pady=50)

# Start the countdown from 3
countdown(3)

# Run the Tkinter event loop
root.mainloop()
