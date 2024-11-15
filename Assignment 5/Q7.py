import tkinter

from tkinter import *

root=tkinter.Tk()
root.geometry("300x300")

def show():
	
	ans=int(e1.get())+int(e2.get())

	e3.delete(0,tkinter.END)
	e3.insert(0,ans)


lb1=Label(root,text="Enter Num 1:")
lb1.place(x=0,y=5)

e1=Entry(root)
e1.place(x=100,y=5)


lb1=Label(root,text="Enter Num 2:")
lb1.place(x=0,y=30)

e2=Entry(root)
e2.place(x=100,y=30)

lb1=Label(root,text=" The Sum Is:")
lb1.place(x=0,y=55)

e3=Entry(root)
e3.place(x=100,y=55)


bt1=Button(root,text="Show",command=show)
bt1.place(x=100,y=80)

bt2=Button(root,text="Quit",command=root.quit)
bt2.place(x=200,y=80)


root.mainloop()