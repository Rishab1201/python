from tkinter import *
from tkinter import messagebox
root  =Tk()
root.geometry('200x200')
def onclick():
    messagebox.showinfo('alert message')

root.title('Message')
button = Button(root,text ='click here',command = onclick)

button.pack()
root.mainloop()