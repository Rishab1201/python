import tkinter as tk

root = tk.Tk()

def change_color(color):
    root.config(bg=color)

menubar = tk.Menu(root)

color_menu = tk.Menu(menubar, tearoff=0)
color_menu.add_command(label='red', command=lambda:change_color("red"))
color_menu.add_command(label='blue', command=lambda:change_color("blue"))
color_menu.add_command(label='black', command=lambda:change_color("black"))
color_menu.add_command(label="green", command=lambda :change_color("green"))

menubar.add_cascade(label="Color", menu=color_menu)

root.config(menu=menubar)

root.mainloop()