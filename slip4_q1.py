import tkinter as tk
import random
def change_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    color = f"#{r:02x}{g:02x}{b:02x}"

    root.configure(background=color)
    root.after(1000, change_color)

root = tk.Tk()

root.geometry("1000x1000")

root.after(1000, change_color)

root.mainloop()
