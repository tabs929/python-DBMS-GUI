from tkinter import Tk,Label,Button
import sqlite3

conn=sqlite3.connect('client.db')

c=conn.cursor()

class app:
    def __init__(self, master):
        self.master=master
        
        self.left= Frame(master,width=400,height =400)
        self.left.pack()
        
        self.right=Frame(master,width=400,height=400)
        self.right.pack()
        
root= Tk()
b= app(root)

root.geometry("1200x270+0+0")
root.resizeable(False,False)
root.mainloop