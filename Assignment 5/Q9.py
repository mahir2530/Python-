import tkinter

from tkinter import *

root=tkinter.Tk()
root.geometry("300x300")

def show(event):

	sel1=l1.curselection()
	sel2=l1.get(sel1)
	lab.config(text=sel2)


lang=['PHP','ROR','PYTHON','ANDROID','IOS']

l1=Listbox(root,width=10)

for i in lang:
	l1.insert(END,i)
	l1.pack()


l1.bind("<<ListboxSelect>>",show)

lab=Label(root)
lab.pack()


root.mainloop()