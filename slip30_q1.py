import tkinter as tk
def String():

    str = entry.get()

    n = entry1.get()

    cnt = 0
    for i in str:
        if i == n:
            cnt += 1

    result.delete('1.0', tk.END)
    result.insert(tk.END, f"Occurrences of {n} in {str} : {cnt}")

root = tk.Tk()

label = tk.Label(root, text='Enter a string :', font=(11))
label.pack()

entry = tk.Entry(root)
entry.pack()

label1 = tk.Label(root, text='Enter a character to search : ', font=(11))
label1.pack()

entry1 = tk.Entry(root)
entry1.pack()

submit_button = tk.Button(root, text='Click', command=String)
submit_button.pack()

result = tk.Text(root,font=(11))
result.pack()

root.mainloop()