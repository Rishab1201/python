import tkinter as tk

def update_string(event=None):
    font_names = font_name.get()
    font_sizes = font_size.get()
    font_weight = "bold" if bold_var.get() else "normal"
    label.config(font=(font_names, font_sizes, font_weight))


root = tk.Tk()
root.title("FONT UPDATE")
label = tk.Label(root,text="Hello World!",font=("Helvetica", 16))
label.pack()

font_name = tk.StringVar(value="Helvetica")
font_name_list = ["Helvetica", "Arial", "Times New Roman", "Courier New"]
font_name_menu = tk.OptionMenu(root, font_name, *font_name_list, command=update_string)
font_name_menu.pack()

font_size = tk.StringVar(value="16")
font_size_list = ["10", "12", "14", "16", "18", "20", "22", "24", "28", "32", "36", "40", "48", "56", "64", "72"]
font_size_menu = tk.OptionMenu(root, font_size, *font_size_list, command=update_string)
font_size_menu.pack()

bold_var = tk.BooleanVar(value=False)
bold_check = tk.Checkbutton(root, text="bold", variable=bold_var, command=update_string)
bold_check.pack()

root.mainloop()