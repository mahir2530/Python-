import tkinter

from tkinter import *

root=tkinter.Tk()

root.geometry("300x300")

def show():


	if var1.get()==1 & var2.get()==1:
		sel="Male , Female"

	elif var1.get()==0 and var2.get()==0:
		sel="Not Selected"


	elif var1.get()==1:
		sel="Male"

	elif var2.get()==1:
		sel="Female"

	lab.config(text=sel)



lb1=Label(root,text="Please Select")
lb1.pack()

var1=IntVar()
var2=IntVar()

chk1=Checkbutton(root,text="Male",variable=var1)
chk1.pack()

chk1=Checkbutton(root,text="Female",variable=var2)
chk1.pack()

bt1=Button(root,text="Show",command=show)
bt1.pack()

bt2=Button(root,text="Quit",command=root.quit)
bt2.pack()


lab=Label(root)
lab.pack()

root.mainloop()