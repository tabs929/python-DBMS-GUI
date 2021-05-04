from tkinter import *

import os

import sys

import sqlite3

import tkinter.messagebox

conn=sqlite3.connect('C:/Users/DELL/Desktop/dbms kurs/client.db')

c=conn.cursor()

class Application:
    def __init__(self, master):
        self.master = master

        # heading label
        self.heading = Label(master, text="UPDATE/DELETE",  fg='gray', font=('arial 38 bold'))
        self.heading.place(x=150, y=0)

        # search criteria -->name 
        self.name = Label(master, text="client's folio_no:", font=('arial 18 bold'))
        self.name.place(x=0, y=60)

        # entry for  the name
        self.namenet = Entry(master, width=30)
        self.namenet.place(x=280, y=70)

        self.search = Button(master, text="Search", width=12, height=1, bg='steelblue',command=self.search_db)
        self.search.place(x=350, y=102)

    def search_db(self):
        self.input = self.namenet.get()

        sql = "SELECT * FROM customer WHERE folio_no LIKE ?"
        self.res = c.execute(sql, (self.input,))
        for self.row in self.res:
            self.folio = self.row[0]
            self.name = self.row[1]
            self.pan_no = self.row[2]
            self.add = self.row[3]
            self.phone = self.row[4]
            self.type_of = self.row[5]

        print(self.folio,self.name,self.pan_no,self.add,self.phone,self.type_of)
    

        #labels
        self.uname = Label(self.master, text="Name", font=('arial 18 bold'))
        self.uname.place(x=0, y=140)

        self.upan_no = Label(self.master, text="Pan_no", font=('arial 18 bold'))
        self.upan_no.place(x=0, y=180)

        self.utype = Label(self.master, text="type_of", font=('arial 18 bold'))
        self.utype.place(x=0, y=220)

        self.uadd = Label(self.master, text="Address", font=('arial 18 bold'))
        self.uadd.place(x=0, y=260)

        self.uphone = Label(self.master, text="Phone Number", font=('arial 18 bold'))
        self.uphone.place(x=0, y=300)

        #entries
        self.ent1 = Entry(self.master, width=30)
        self.ent1.place(x=280, y=140)
        self.ent1.insert(END, str(self.name))

        self.ent2 = Entry(self.master, width=30)
        self.ent2.place(x=280, y=180)
        self.ent2.insert(END, str(self.pan_no))

        self.ent3 = Entry(self.master, width=30)
        self.ent3.place(x=280, y=220)
        self.ent3.insert(END, str(self.type_of))

        self.ent4 = Entry(self.master, width=30)
        self.ent4.place(x=280, y=260)
        self.ent4.insert(END, str(self.add))

        self.ent5 = Entry(self.master, width=30)
        self.ent5.place(x=280, y=300)
        self.ent5.insert(END, str(self.phone))

        self.update = Button(self.master, text="Update", width=20, height=2, bg='lightblue', command=self.update_db)
        self.update.place(x=350, y=380)

        # button to delete
        self.delete = Button(self.master, text="Delete", width=20, height=2, bg='red', command=self.delete_db)
        self.delete.place(x=150, y=380)

    def update_db(self):
        self.var1 = self.ent1.get() #nm
        self.var2 = self.ent2.get() #pan
        self.var3 = self.ent3.get() #ty
        self.var4 = self.ent4.get() #ad
        self.var5 = int(self.ent5.get()) #po
        self.var6 = self.folio

        dets=(self.var6,self.var1, self.var2, self.var4, self.var5,self.var3,self.var6)
        print(dets)
        query = "UPDATE customer SET folio_no=? ,name=?, pan_no=?, address=?, phone_no=?, type_of=? WHERE folio_no LIKE ?"
        c.execute(query,dets)
        conn.commit()
        tkinter.messagebox.showinfo("Updated", "Successfully Updated.")

    def delete_db(self):
        # delete the appointment
        sql2 = "DELETE FROM customer WHERE folio_no LIKE ?"
        c.execute(sql2,(self.namenet.get()))
        conn.commit()
        tkinter.messagebox.showinfo("Success", "Deleted Successfully")
        self.ent1.destroy()
        self.ent2.destroy()
        self.ent3.destroy()
        self.ent4.destroy()
        self.ent5.destroy()  

root = Tk()
b = Application(root)

root.geometry("720x550+0+0")

root.resizable(False, False)

root.mainloop()