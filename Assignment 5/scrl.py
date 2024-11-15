import tkinter

from tkinter import *

root=tkinter.Tk()

root.geometry("300x300")

c=Canvas(root)
'''


c.create_line(5,50,250,250)

c.create_line(5,250,250,50)

c.create_line(5,150,250,150)

c.create_line(128,50,128,250)

c.create_line(128,50,128,250)

'''

c.create_rectangle(35,50,260,250)

c.create_oval(35,50,260,250)

c.create_arc(100,80,250,230,start=0,extent=-180)




c.pack()


root.mainloop()