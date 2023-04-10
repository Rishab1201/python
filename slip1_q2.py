from tkinter import *
from datetime import date
def age():
    year = int(y.get())

    result =  - year

    print("Age :- ", result)
    res.config(text=result)

root = Tk()

label1 = Label(root,text='DAY')
d = Entry(root)

label2 = Label(root,text='MONTH')
m = Entry(root)

label3 = Label(root,text='YEAR')
y = Entry(root)

res = Label(root,text='result')

button = Button(root,text='click me',command=age)

label1.grid(row=0 , column= 0)
d.grid(row=0,column=1)

label2.grid(row=1,column=0)
m.grid(row=1,column=1)

label3.grid(row=2,column=0)
y.grid(row=2,column=1)

res.grid(row=3,column=1,columnspan=2)

button.grid(row=4,column=1,columnspan=2)

root.mainloop()