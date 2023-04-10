import tkinter as tk

def add():
    num1 = float(Ip_1.get())
    num2 = float(Ip_2.get())
    Result = num1 + num2
    print("Result",Result)
    res_label.config(text = Result)


root = tk.Tk()
root.title("Add two numbers")

label_1 = tk.Label(root,text = 'Num_1')

Ip_1 = tk.Entry(root)

label_2 = tk.Label(root, text = 'Num_2')

Ip_2 = tk.Entry(root)

add_button = tk.Button(root,text = 'Add',command = add)

res_label = tk.Label(root,text = 'Result')

label_1.grid(row = 0,column = 0)
Ip_1.grid(row = 0 ,column = 1)
label_2.grid(row = 1,column = 0)
Ip_2.grid(row = 1,column = 1)
add_button.grid(row = 2,column = 0,columnspan = 2)
res_label.grid(row = 3,column = 0,columnspan = 2)

root.mainloop()