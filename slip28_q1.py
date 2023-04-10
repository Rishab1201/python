import tkinter as tk

root = tk.Tk()

list_box = tk.Listbox(root, cursor='')
list_box.insert(1, 'Python')
list_box.insert(2, 'CPP')
list_box.insert(3, 'OOSE')
list_box.insert(4, 'Big Data')

list_box.pack()

root.mainloop()