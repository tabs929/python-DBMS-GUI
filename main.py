from tkinter import *

import os

import sys


class Application:
    def __init__(self,master):
        self.master=master

        self.heading = Label(text="investment portfolio DBMS",font=('arial 28 bold'), fg='white', bg='gray')
        self.heading.place(x=70, y=0)

        self.addets = Button(text="ADD DETAILS", width=20, height=2, bg='lightblue',command=self.add_details)
        self.addets.place(x=50, y=100)

        self.update =Button(text="UPDATE/DELETE" ,width=20, height=2, bg='lightblue',command=self.go_to)
        self.update.place(x=250, y=100)

        self.update =Button(text="DISPLAY" ,width=20, height=2, bg='lightblue',command=self.dis)
        self.update.place(x=450, y=100)

    def add_details(self):
        import course
        exec("C:/Users/DELL/Desktop/dbms kurs/course.py")

    def go_to(self):
        import update
        exec("C:/Users/DELL/Desktop/dbms kurs/update.py")

    def dis(self):
        import display
        exec("C:/Users/DELL/Desktop/dbms kurs/display.py")

root = Tk()
b = Application(root)

root.geometry("640x200+0+0")

root.resizable(False, False)

root.mainloop()