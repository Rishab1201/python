import tkinter as tk

def update_font(event=None):
    font_name = font_names.get()
    font_size = font_sizes.get()
    font_weight = "bold" if bold_var.get() else "normal"
    label.config(font=(font_name, font_size, font_weight))

root = tk.Tk()
root.title("Font Changer")

label = tk.Label(root, text="Hello, world!", font=("Helvetica", 16))
label.pack()

font_names = tk.StringVar(value="Helvetica")
font_names_list = ["Helvetica", "Arial", "Times New Roman", "Courier New"]
font_names_menu = tk.OptionMenu(root, font_names, *font_names_list, command=update_font)
font_names_menu.pack()

font_sizes = tk.StringVar(value="16")
font_sizes_list = ["10", "12", "14", "16", "18", "20", "22", "24", "28", "32", "36", "40", "48", "56", "64", "72"]
font_sizes_menu = tk.OptionMenu(root, font_sizes, *font_sizes_list, command=update_font)
font_sizes_menu.pack()

bold_var = tk.BooleanVar(value=False)
bold_check = tk.Checkbutton(root, text="Bold", variable=bold_var, command=update_font)
bold_check.pack()

root.mainloop()
