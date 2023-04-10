import tkinter as tk

def multi():

    n = int(entry.get())
    result.delete('1.0',tk.END)
    for i in range(1, 11):
        result.insert(tk.END,f"{n} x {i} = {n*i} \n")


root = tk.Tk()

root.title("Multiplication Table")

label = tk.Label(text='Enter a number : ')
label.pack()

entry = tk.Entry()
entry.pack()

submit = tk.Button(text="click", command=multi)
submit.pack()

result = tk.Text(root)
result.pack()

root.geometry("250x250")
root.mainloop()