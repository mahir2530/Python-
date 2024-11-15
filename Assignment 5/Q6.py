import tkinter

from tkinter import *

root=tkinter.Tk()
root.geometry("300x300")

list1=['red','yellow','pink','green','purple','orange','blue']

for i in list1:

	lb1=Label(root,text=i,bg=i,width=10)
	lb1.pack()

root.mainloop()