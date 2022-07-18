from tkinter import *
import sqlite3
root=Tk()
root.geometry('500x400')
root.title("Information")

Fullname = StringVar()
Email = StringVar()
var = StringVar(root,0)
c = StringVar()
var1 = StringVar(root,0)
Category=StringVar()
event_category=StringVar()



def asc_data():
    obj=Tk()
    obj.geometry('350x400')
    obj.title("Price lowest to highest")
    conn = sqlite3.connect('Project.db')
    cursor = conn.cursor()
    t1 = []
    count = 0
    r1=1
    c1=0
    Label(obj,text="Name ").grid(row=0,column=0)
    Label(obj,text="Start Location ").grid(row=0,column=1)
    Label(obj,text="Destination ").grid(row=0,column=2)
    Label(obj,text="Price ").grid(row=0,column=3)
    Label(obj,text="Bus ID ").grid(row=0,column=4)
    x = cursor.execute("\nSelect * from HeritageWalk order by price ASC ",t1)
    for row in x.fetchall():
        for i in range(0, 5):
            Label(obj, text=row[i]).grid(row=r1,column=c1)
            c1 = c1 + 1
        c1 = 0
        r1 = r1 + 1
        count += 1
    mainloop()
    cursor.close()
    conn.close()



def dec_data():
    obj1=Tk()
    conn = sqlite3.connect('Project.db')
    obj1.geometry('350x400')
    obj1.title("Price Highest to Lowest")
    r2 = 1
    c2 = 0
    cursor = conn.cursor()
    t2 = []
    count = 0
    Label(obj1, text="Name ").grid(row=0, column=0)
    Label(obj1, text="Start Location ").grid(row=0, column=1)
    Label(obj1, text="Destination ").grid(row=0, column=2)
    Label(obj1, text="Price ").grid(row=0, column=3)
    Label(obj1, text="Bus ID ").grid(row=0, column=4)
    y = cursor.execute("Select * from HeritageWalk order by price DESC ",t2)
    for row in y.fetchall():
        for i in range(0, 5):
            Label(obj1, text=row[i]).grid(row=r2,column=c2)
            c2 = c2 + 1
        c2 = 0
        r2 = r2 + 1
        count += 1
    mainloop()
    cursor.close()
    conn.close()


def max_data():
    obj3=Tk()
    obj3.geometry('350x100')
    obj3.title("Highest Priced")
    r3 = 1
    c3 = 0
    conn = sqlite3.connect('Project.db')
    cursor = conn.cursor()
    t3 = []
    count = 0
    Label(obj3, text="Name ").grid(row=0, column=0)
    Label(obj3, text="Start Location ").grid(row=0, column=1)
    Label(obj3, text="Destination ").grid(row=0, column=2)
    Label(obj3, text="Price ").grid(row=0, column=3)
    Label(obj3, text="Bus ID ").grid(row=0, column=4)
    z = cursor.execute("select * from HeritageWalk where price=(SELECT min(price) from HeritageWalk) ",t3)
    for row in z.fetchall():
        for i in range(0, 5):
            Label(obj3, text=row[i]).grid(row=r3,column=c3)
            c3 = c3 + 1
        c3 = 0
        r3 = r3 + 1
        count += 1
    mainloop()
    cursor.close()
    conn.close()


def min_data():
    obj4=Tk()
    obj4.geometry('350x100')
    obj4.title("Lowest Priced")
    r4 = 1
    c4 = 0
    conn = sqlite3.connect('Project.db')
    cursor = conn.cursor()
    t4 = []
    count = 0
    Label(obj4, text="Name ").grid(row=0, column=0)
    Label(obj4, text="Start Location ").grid(row=0, column=1)
    Label(obj4, text="Destination ").grid(row=0, column=2)
    Label(obj4, text="Price ").grid(row=0, column=3)
    Label(obj4, text="Bus ID ").grid(row=0, column=4)
    a = cursor.execute("select * from HeritageWalk where price=(SELECT max(price) from HeritageWalk) ",t4)
    for row in a.fetchall():
        for i in range(0, 5):
            Label(obj4, text=row[i]).grid(row=r4,column=c4)
            c4 = c4 + 1
        c4 = 0
        r4 = r4 + 1
        count += 1


    mainloop()
    cursor.close()
    conn.close()


label_0 = Label(root, text=" Heritage Walk ", width=20, font=("bold", 30))
label_0.place(x=30, y=20)

label_1 = Label(root, text=" Event prices from low to high ", width=30, font=("bold", 12))
label_2 = Label(root, text=" Event prices from high to low ", width=30, font=("bold", 12))
label_3 = Label(root, text=" Lowest Priced Deal  ", width=30, font=("bold", 12))
label_4 = Label(root, text=" Highest Priced Deal  ", width=30, font=("bold", 12))
label_1.place(x=10, y=100)
label_2.place(x=10, y=150)
label_3.place(x=20, y=200)
label_4.place(x=20, y=250)


Button(root, text='View', width=20, bg='brown', fg='white', command=asc_data ).place(x=300, y=100)
Button(root, text='View', width=20, bg='brown', fg='white', command=dec_data).place(x=300, y=150)
Button(root, text='View', width=20, bg='brown', fg='white', command=max_data).place(x=300, y=200)
Button(root, text='View', width=20, bg='brown', fg='white', command=min_data).place(x=300, y=250)

root.mainloop()

