import tkinter as tk
def decimal():
    decimal_num = int(entry.get())

    result.delete('1.0', tk.END)
    binary_num = bin(decimal_num)

    result.insert(tk.END, f"Binary Number : {binary_num}\n")

    octa_num = oct(decimal_num)

    result.insert(tk.END, f"Octal Number : {octa_num}\n")

    hex_num = hex(decimal_num)

    result.insert(tk.END, f"Hexadecimal Number : {hex_num}\n")


root = tk.Tk()

label = tk.Label(root, text='Enter a Decimal Number : ')
label.pack()

entry = tk.Entry(root)
entry.pack()

submit_button = tk.Button(root, text='Submit', command=decimal)
submit_button.pack()

result = tk.Text(root)
result.pack()

root.mainloop()