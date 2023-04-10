import tkinter as tk

def add_item():
    item = item_entry.get()
    if item:
        listbox.insert(tk.END, item)
        item_entry.delete(0, tk.END)

def print_items():
    for i in listbox.curselection():
        print(listbox.get(i))

def delete_items():
    for i in reversed(listbox.curselection()):
        listbox.delete(i)

root = tk.Tk()
root.title("Listbox Example")

item_label = tk.Label(root, text="Item:")
item_label.pack()

item_entry = tk.Entry(root)
item_entry.pack()

add_button = tk.Button(root, text="Add", command=add_item)
add_button.pack()

listbox = tk.Listbox(root)
listbox.pack()

print_button = tk.Button(root, text="Print Selected", command=print_items)
print_button.pack()

delete_button = tk.Button(root, text="Delete Selected", command=delete_items)
delete_button.pack()

root.mainloop()
