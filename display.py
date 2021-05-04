from tkinter import *

import sqlite3

import tkinter.messagebox

import pandas as pd

conn=sqlite3.connect('C:/Users/DELL/Desktop/dbms kurs/client.db')


c=conn.cursor()

class Records:
        def __init__(self, master):
            self.master = master

            self.heading = Label(text="RECORDS",font=('arial 28 bold'), fg='white', bg='gray')
            self.heading.grid(row=0,column=0)
 
            self.textLabel = Label(self.master, text="FOLIO NO", width=10)
            self.textLabel.grid(row=3, column=0)
            
            self.intLabel = Label(self.master, text="NAME", width=10)
            self.intLabel.grid(row=3, column=1)
            
            self.intLabel = Label(self.master, text="PAN NO", width=10)
            self.intLabel.grid(row=3, column=2)
            
            self.intLabel = Label(self.master, text="ADDRESS", width=10)
            self.intLabel.grid(row=3, column=3)
            
            self.intLabel = Label(self.master, text="PHONE NO", width=10)
            self.intLabel.grid(row=3, column=4)

            self.intLabel = Label(self.master, text="TYPE", width=10)
            self.intLabel.grid(row=3, column=5)

            self.showallrecords()

        def showallrecords(self):
            Data=self.readfromdatabase()
            for index, dat in enumerate(Data):
                Label(self.master, text=dat[0]).grid(row=index+4, column=0)
                Label(self.master, text=dat[1]).grid(row=index+4, column=1)
                Label(self.master, text=dat[2]).grid(row=index+4, column=2)
                Label(self.master, text=dat[3]).grid(row=index+4, column=3)
                Label(self.master, text=dat[4]).grid(row=index+4, column=4)
                Label(self.master, text=dat[5]).grid(row=index+4, column=5)
        
        def readfromdatabase(self):
            c.execute("SELECT * FROM customer")
            return c.fetchall()
    

root = Tk()
root.title("RECORDS")
b = Records(root)

root.geometry("600x500+0+0")

root.resizable(False, False)

root.mainloop()
    