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

def fetch_all_data():
    obj=Tk()
    obj.geometry('500x500')
    obj.title("All Event Details")
    conn = sqlite3.connect('Project.db')
    cursor = conn.cursor()
    t = []
    count = 0
    r2 = 1
    c2 = 0
    Label(obj, text="Performer Name ").grid(row=0, column=0)
    Label(obj, text="Event Category").grid(row=0, column=1)
    Label(obj, text="Event Location").grid(row=0, column=2)
    Label(obj, text="Event Date").grid(row=0, column=3)
    Label(obj, text="Event Time").grid(row=0, column=4)
    x = cursor.execute("select performer_name,event_category,event_location,event_date,event_time from Performers NATURAL JOIN Events")
    for row in x.fetchall():
        for i in range(0, 5):
            Label(obj, text=row[i]).grid(row=r2,column=c2)
            c2 = c2 + 1
        c2 = 0
        r2 = r2 + 2
        count += 1
    mainloop()
    cursor.close()
    conn.close()


def fetch_selective_data():
    obj1=Tk()
    obj1.title("Specific Event Details")
    obj1.geometry('500x200')
    conn = sqlite3.connect('Project.db')
    cursor = conn.cursor()
    t1 = []
    count = 0
    r1 = 1
    c1 = 0
    Label(obj1, text="Performer Name ").grid(row=0, column=0)
    Label(obj1, text="Event Category").grid(row=0, column=1)
    Label(obj1, text="Event Location").grid(row=0, column=2)
    Label(obj1, text="Event Date").grid(row=0, column=3)
    Label(obj1, text="Event Time").grid(row=0, column=4)
    t1.append(c.get())
    y = cursor.execute("select performer_name,event_category,event_location,event_date,event_time from Performers NATURAL JOIN Events where event_category = ?",t1)
    for row in y.fetchall():
        for i in range(0, 5):
            Label(obj1, text=row[i]).grid(row=r1,column=c1)
            c1 = c1 + 1
        c1 = 0
        r1 = r1 + 1
        count += 1
    mainloop()
    cursor.close()
    conn.close()


label_0 = Label(root, text="""Select from category """, width=20, font=("bold", 15))
label_0.place(x=150, y=190)

list1 = ['Children', 'Films', 'Dance', 'Food', 'Music', 'Literature','Workshop']

droplist = OptionMenu(root,c, *list1)
droplist.config(width=18)
c.set('Options')
droplist.place(x=180, y=250)

Label(root,text="Event Details",width=25,font=("bold",25)).place(x=10,y=10)
Button(root, text='All Event Details', width=30, bg='brown', fg='white', command=fetch_all_data).place(x=150, y=100)
Button(root, text='View', width=10, bg='brown', fg='white', command=fetch_selective_data).place(x=215, y=320)

root.mainloop()

