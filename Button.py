from tkinter import*

parent = Tk()

def demo():
    print('hello world')

parent.geometry('500x250')

btn = Button(parent,text="Hello",command=demo)

btn.pack()


parent.mainloop()