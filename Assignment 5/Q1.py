import tkinter

from tkinter import messagebox

root=tkinter.Tk()
root.geometry("300x300")

def show():

	messagebox.showinfo("Hello","This Is Question 1")


bt1=tkinter.Button(root,text="Click Me",command=show)
bt1.pack()


root.mainloop()