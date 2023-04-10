
#pack () example

from tkinter import*
parent = Tk()

rb = Button(parent,text = 'red',fg='red')

rb.pack(side=TOP)

gb = Button(parent,text='black')

gb.pack(side=BOTTOM)
parent.mainloop()