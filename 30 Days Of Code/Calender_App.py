import tkinter as tk
from tkinter import *
import calendar

r = tk.Tk()
r.title("Calender App")
r.geometry("300x200")
r.resizable(width=False, height=False)

def show_cal():
    m = int(m_s.get())
    y = int(y_s.get())
    cal = calendar.month(y,m)
    
    dis.insert("end", cal)
    
def clear():
    dis.delete(1.0, "end")

dis = Text(r, width=33, height=8, relief=RIDGE, borderwidth=2)
dis.place(x=13, y=1)

L = Label(r, text = "Month", width = 9)
L.place(x=1, y=170)

m_s = Spinbox(r, from_=1, to=12, width = 8)
m_s.place(x=60, y = 170)

L2 = Label(r, text="Year",width=9)
L2.place(x = 170, y = 170)

y_s = Spinbox(r, from_=1900, to=2100, width = 8)
y_s.place(x=220, y = 170)

show = Button(r, text = "Display", width = 8, command=show_cal)
show.place(x = 13, y =140)

clear = Button(r, text = "Delete", width = 5, command=clear)
clear.place(x = 78, y = 140)

exit = Button(r, text = "exit", width = 5, command=r.destroy)
exit.place(x = 240, y = 140)

r.mainloop()