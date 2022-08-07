from ast import Delete
import tkinter as tk
import mysql.connector
from tkinter import *

#connect DB
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='mydatabse'
)
#window
root = tk.Tk()
root.geometry('500x500')
root.title('Python Form')
heading = Label(text = 'Python Form', fg = 'black',)
heading.grid()

#Name entry label
entry_label = tk.Label(root, text='Name')
entry_label.grid(column=0, row=1)

#Name entry
name = tk.Entry()
name.grid(column= 1, row=1)

#address entry
address = tk.Entry()
address.grid(column= 3, row=1)

#address entry Label
address_entry_label = tk.Label(root, text='Address')
address_entry_label.grid(column=2, row=1)

#enable communication
mycursor = mydb.cursor()

#creating database
    #mycursor.execute('CREATE DATABASE mydatabse')
    #mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))"

#instert to database with button press
def submit_entry():
    #get strings from entries
    name_string = str(name.get())
    address_string = str(address.get())
    #define sql entries
    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    val = (name_string, address_string)
    #execute
    mycursor.execute(sql, val)
    #submit entries
    mydb.commit()
    #clear fields
    name.delete(0,END)
    address.delete(0,END)
    #display success
    submitted_label = tk.Label(root, text='Submitted')
    submitted_label.grid(column=0, row=4)

#submit button with command
submit_text = tk.StringVar()
submit_btn = tk.Button(root, textvariable=submit_text, font='Calibri', bg='blue', fg='white', height=2, width=15, command=submit_entry)
submit_text.set('Submit')
submit_btn.grid(column=0, row=3)

#close window loop
root.mainloop()