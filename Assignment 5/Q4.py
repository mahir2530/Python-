import tkinter

from tkinter import * 

root=tkinter.Tk()

root.geometry("300x300")

def show():

	if var1.get()==1:

		sel="You Are Not Eligible :("


	elif var1.get()==2:

		sel="You Are Eligible :)"

	lab.config(text=sel)



var1=IntVar()



rd1=Radiobutton(root,text="Less Than 18",variable=var1,value=1,command=show)
rd1.pack()


rd1=Radiobutton(root,text="Greater Than 18",variable=var1,value=2,command=show)
rd1.pack()

lab=Label(root)
lab.pack()


root.mainloop()