import tkinter as tk

def volume():
    r = int(entry.get())

    vol = 4/3 * 3.14 * r * r *r

    result.delete('1.0', tk.END)
    result.insert(tk.END, f"Volume of Sphere : {vol}")


root = tk.Tk()

label = tk.Label(root, text='Enter Radius of Sphere : ')
label.pack()

entry = tk.Entry(root)
entry.pack()

submit_button = tk.Button(root, text='Click', command=volume)
submit_button.pack()

result = tk.Text(root)
result.pack()

root.mainloop()