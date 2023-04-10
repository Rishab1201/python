# grid() example

from tkinter import*

parent = Tk()

name = Label(parent,text='name').grid(row=0,column=0)

lname = Label(parent,text='Last name').grid(row=1,column=0)

el = Entry(parent).grid(row=0,column=1)
el1 = Entry(parent).grid(row=1,column=1)

parent.mainloop()

