import random,string
from tkinter import *


def pass_generator():
    password = ""
    combi = [string.ascii_uppercase, string.ascii_lowercase]
    for p in range(pass_len.get()):
        char_val = random.choice(combi)
        password = password + random.choice(char_val)

    print(password)
    out_put.config(text=password)

root =Tk()
root.geometry('200x200')
pass_len = IntVar()
pass_label = Label(root, text='password length')
Entry(root, textvariable=pass_len).pack()
Button(root, command=pass_generator, text='generate', font='arial 10').pack()

out_put = Label(root,text="password")
out_put.pack()

root.mainloop()
