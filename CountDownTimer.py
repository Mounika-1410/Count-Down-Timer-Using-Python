import tkinter as tk
from tkinter import messagebox

class CountdownTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("CountDown Timer")
        
        # Initialize time values
        self.hours = 0
        self.minutes = 5
        self.seconds = 10
        self.timer_running = False
        self.time_left = None

        # Create the time input section
        self.time_label = tk.Label(self.root, text="Set Time", font=("Helvetica", 18, "bold"), bg="gray", fg="yellow")
        self.time_label.grid(row=0, column=1, pady=10)

        # Hour, minute, second input fields
        self.hour_entry = tk.Spinbox(self.root, from_=0, to=23, width=5)
        self.hour_entry.grid(row=1, column=0, padx=5)

        self.minute_entry = tk.Spinbox(self.root, from_=0, to=59, width=5)
        self.minute_entry.grid(row=1, column=1, padx=5)

        self.second_entry = tk.Spinbox(self.root, from_=0, to=59, width=5)
        self.second_entry.grid(row=1, column=2, padx=5)

        # Buttons
        self.cancel_button = tk.Button(self.root, text="Cancel", command=self.cancel_timer, width=10)
        self.cancel_button.grid(row=2, column=0, pady=10)

        self.set_button = tk.Button(self.root, text="Set", command=self.set_timer, width=10)
        self.set_button.grid(row=2, column=1, pady=10)

        self.start_button = tk.Button(self.root, text="Start", command=self.start_timer, bg="green", fg="white", width=10)
        self.start_button.grid(row=2, column=2, pady=10)

        self.pause_button = tk.Button(self.root, text="Pause", command=self.pause_timer, bg="red", fg="white", width=10)
        self.pause_button.grid(row=3, column=1, pady=10)

        # Time Left label
        self.time_left_label = tk.Label(self.root, text="Time Left: 0: 0: 0", font=("Helvetica", 18), bg="gray", fg="yellow")
        self.time_left_label.grid(row=4, column=1, pady=10)

        # Update the time label every second
        self.update_time()

    def set_timer(self):
        try:
            self.hours = int(self.hour_entry.get())
            self.minutes = int(self.minute_entry.get())
            self.seconds = int(self.second_entry.get())
            self.time_left = self.hours * 3600 + self.minutes * 60 + self.seconds
            self.update_time()
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numbers for time.")
    
    def update_time(self):
        if self.time_left is not None:
            hours = self.time_left // 3600
            minutes = (self.time_left % 3600) // 60
            seconds = self.time_left % 60
            self.time_left_label.config(text=f"Time Left: {hours}: {minutes}: {seconds}")
        if self.timer_running and self.time_left > 0:
            self.time_left -= 1
            self.root.after(1000, self.update_time)
    
    def start_timer(self):
        if self.time_left is not None and self.time_left > 0:
            self.timer_running = True
            self.update_time()
        else:
            messagebox.showerror("No Time Set", "Please set the time first.")

    def pause_timer(self):
        self.timer_running = False

    def cancel_timer(self):
        self.timer_running = False
        self.time_left = None
        self.update_time()

if __name__ == "__main__":
    root = tk.Tk()
    timer = CountdownTimer(root)
    root.mainloop()
