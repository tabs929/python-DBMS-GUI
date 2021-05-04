from tkinter import *

import os

import sys

import sqlite3

import tkinter.messagebox

conn=sqlite3.connect('C:/Users/DELL/Desktop/dbms kurs/client.db')


c=conn.cursor()


class Application:
    def __init__(self,master):
        self.master=master

        self.left = Frame(master, width=1200, height=720, bg='lightgray')
        self.left.pack(side=LEFT)

        self.heading = Label(self.left,text="ADD DETAILS",font=('arial 28 bold'), fg='white', bg='gray')
        self.heading.place(x=0, y=0)

        self.foliono = Label(self.left,text="FOLIO NUMBER:", font=('arial 18 bold'), fg='black',bg='lightgray')
        self.foliono.place(x=0, y=100)

        self.name = Label(self.left,text="CLIENT NAME:", font=('arial 18 bold'), fg='black',bg='lightgray')
        self.name.place(x=0, y=140)

        self.pannum= Label(self.left,text="PAN NUMBER:", font=('arial 18 bold'), fg='black',bg='lightgray')
        self.pannum.place(x=0, y=180)

        self.type_of = Label(self.left,text="TYPE OF INVESTMENT:", font=('arial 18 bold'), fg='black',bg='lightgray')
        self.type_of.place(x=0, y=220)

        self.address= Label(self.left,text="CLIENT ADDRESS:", font=('arial 18 bold'), fg='black',bg='lightgray')
        self.address.place(x=0, y=260)

        self.phone= Label(self.left,text="PHONE NUMBER:", font=('arial 18 bold'), fg='black',bg='lightgray')
        self.phone.place(x=0, y=300)

        #entries
        self.folio_ent = Entry(self.left, width=30)
        self.folio_ent.place(x=276, y=110)

        self.name_ent = Entry(self.left, width=30)
        self.name_ent.place(x=276, y=150)

        self.pannum_ent = Entry(self.left, width=30)
        self.pannum_ent.place(x=276, y=190)

        self.type_ent = Entry(self.left, width=30)
        self.type_ent.place(x=276, y=230)

        self.add_ent = Entry(self.left, width=30)
        self.add_ent.place(x=276, y=270)

        self.phone_ent = Entry(self.left, width=30)
        self.phone_ent.place(x=276, y=310)
        #button
        self.submit = Button(self.left,text="ADD DETAILS", width=20, height=2, bg='lightblue',command=self.add_details)
        self.submit.place(x=200, y=360)
        '''
        self.update =Button(self.left,text="UPDATE" ,width=20, height=2, bg='lightblue',command=self.go_to)
        self.update.place(x=250, y=360)
        '''    
    def add_details(self):
        self.val1 = int(self.folio_ent.get())
        self.val2 = self.name_ent.get()
        self.val3 = self.pannum_ent.get()
        self.val4 = self.add_ent.get()
        self.val5 = int(self.phone_ent.get())
        self.val6 = self.type_ent.get()
        data = (self.val1, self.val2, self.val3, self.val4, self.val5,self.val6)
        print(data)
        if self.val1 == '' or self.val2 == '' or self.val3 == '' or self.val4 == '' or self.val5 == '' or self.val6=='':
            tkinter.messagebox.showinfo("Warning", "Please Fill Up All Boxes")
        else:
            # now we add to the database
            sql = """INSERT INTO customer(folio_no,name,pan_no,address,phone_no,type_of) VALUES(? ,?, ?, ?, ?, ?)"""
            c.execute(sql, data)
            conn.commit()
            tkinter.messagebox.showinfo("Success", "data stored for " +str(self.val2) +"!")
    '''
    def go_to(self):
        import update
        exec("C:/Users/DELL/Desktop/dbms kurs/update.py")
    '''

root = Tk()
b = Application(root)

root.geometry("600x500+0+0")

root.resizable(False, False)

root.mainloop()