
import tkinter as tk
from tkinter import messagebox
import datetime
import time


def set_alarm():
    alarm_time = entry.get()
    try:
        datetime.datetime.strptime(alarm_time, "%H:%M")
    except ValueError:
        messagebox.showerror("Error", "Invalid time format. Please enter time in HH:MM format.")
        return

    while True:
        current_time = time.strftime("%H:%M")
        if current_time == alarm_time:
            messagebox.showinfo("Alarm", "Wake up!")
            break


# Create GUI window
window = tk.Tk()
window.title("Alarm Clock")

# Create label
label = tk.Label(window, text="Enter alarm time (HH:MM):")
label.pack()

# Create entry field
entry = tk.Entry(window)
entry.pack()

# Create button
button = tk.Button(window, text="Set Alarm", command=set_alarm)
button.pack()

# Run the GUI
window.mainloop()