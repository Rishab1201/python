import tkinter as tk

def cylinder():
    r = int(entry1.get())
    h = int(entry2.get())

    a = 2 * 3.14 * r * h + 2 * 3.14 * r * r

    v = 3.14 * r * r * h
    result.config(text=f"surface area of cylinder is : {a} \nVolume of cylinder is : {v}\n")


root = tk.Tk()

label1 =tk.Label(text="Enter Radius of cylinder :")
label1.pack()

entry1 = tk.Entry()
entry1.pack()

label2 = tk.Label(text="Enter Height of cylinder :")
label2.pack()

entry2 = tk.Entry();
entry2.pack()

submit_button = tk.Button(text="submit",command=cylinder)
submit_button.pack()

result = tk.Label(text="",font=("Times New Roman", 12))
result.pack()

root.geometry("250x200")

root.mainloop()