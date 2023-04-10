import tkinter as tk
import time

def update_time():
    current_time = time.strftime("%H:%M:%S")
    time_label.config(text=current_time)
    root.after(1000, update_time)

root = tk.Tk()
root.title("Digital Clock")

time_label = tk.Label(root, font=("Arial", 80), bg="black", fg="red")
time_label.pack()

update_time()

root.mainloop()
