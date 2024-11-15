import tkinter

from tkinter import *

root=tkinter.Tk()
root.geometry("350x300")

def show():

	if var1.get()==0:
		sel="Python"

	elif var1.get()==1:
		sel="Perl"

	elif var1.get()==2:
		sel="Java"

	elif var1.get()==3:
		sel="C"

	elif var1.get()==4:
		sel="C++" 

	lab.config(text=sel)






lbl=Label(root,text="Choose Your Favourite Programming Language")
lbl.pack()

lang=['Python','Perl','Java','C','C++']

var1=IntVar()

for i,j in enumerate(lang):

	rd1=Radiobutton(root,text=j,variable=var1,value=i,command=show)
	rd1.pack()


lab=Label(root)
lab.pack()


root.mainloop()