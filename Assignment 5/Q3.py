import tkinter

from tkinter import *

root=tkinter.Tk()
root.geometry("350x300")

def show():

    sel=[]

    if var1.get()==1:
    	sel.append("Banans")

    if var2.get()==1:
    	sel.append("Chicken")

    if var3.get()==1:
    	sel.append("Stuffed Peppers")

    lab.config(text=",".join(sel))


lbl=Label(root,text="Choose Your Favourite Food")
lbl.pack()


var1=IntVar()

var2=IntVar()

var3=IntVar()



chk1 = Checkbutton(root,text="Banans",variable=var1,command=show)
chk1.place(x=5,y=50)

chk2 = Checkbutton(root,text="Chicken",variable=var2,command=show)
chk2.place(x=100,y=50)

chk3 = Checkbutton(root,text="Stuffed Peppers",variable=var3,command=show)
chk3.place(x=200,y=50)


lab=Label(root)
lab.place(x=50,y=100)


root.mainloop()