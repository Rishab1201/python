import tkinter as tk
def String():
    n = entry.get()

    if n.islower():
        str = n.upper()
        result.config(text=f"String in uppercase : {str} ")
    else:
        result.config(text=f"Please enter string in lowercase")


root = tk.Tk()

lable = tk.Label(text="Enter a string : ")
lable.pack()

entry = tk.Entry()
entry.pack()

submit = tk.Button(text="submit", command=String)
submit.pack()

result = tk.Label(font=("Times New Roman", 12))
result.pack()

root.geometry("300x200")
root.mainloop()
