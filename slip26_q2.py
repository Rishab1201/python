import tkinter as tk
def update_string():

    n = entry.get()

    sentence = " "
    for i in n:
        if i.isalpha():
            if i.isupper():
                sentence += i.lower()
            else:
                sentence += i.upper()
        elif i.isdigit():
            sentence += "?"
        elif i.isspace():
            sentence += "*"
        else:
            sentence += i

    result.delete('1.0', tk.END)
    result.insert(tk.END, f"Update Santence is \n{sentence}")

root = tk.Tk()

label = tk.Label(text='Enter a sentence : ')
label.pack()

entry = tk.Entry()
entry.pack()

submit_button = tk.Button(text='Submit', command=update_string)
submit_button.pack()

result = tk.Text(root)
result.pack()

root.mainloop()
