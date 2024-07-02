from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql
import re


def hide():
    openeye.config(file='cl.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)


def show():
    openeye.config(file='op.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)




def clear():
    phoneEntry.delete(0, END)
    usernameEntry.delete(0, END)
    passwordEntry.delete(0, END)
    confirmEntry.delete(0, END)
    check.set(0)



def connect_database():
    if emailEntry.get() == '' or phoneEntry.get() == '' or usernameEntry.get() == '' or passwordEntry.get() == '' or confirmEntry.get() == '':
        messagebox.showerror('error', 'all fields required')

    elif re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',emailEntry.get() ) is None:
        messagebox.showinfo('error', 'invalid mail')

    elif len(phoneEntry.get()) != 10 :
        messagebox.showinfo('error', 'length 10 and only no')
    elif re.match(r'^[6-9]\d{9}$',phoneEntry.get()) is None:
        messagebox.showinfo('error', ' only no')

    elif phoneEntry.get() == phoneEntry.get().isalnum() :
        messagebox.showinfo('error', 'number only')


    elif usernameEntry.get() < '8':
        messagebox.showinfo('error', 'username must be character and less then 8 character')

    elif passwordEntry.get() != confirmEntry.get():
        messagebox.showinfo('error', 'password mismatched ')

    elif passwordEntry.get() < '8':
        messagebox.showinfo('error', 'password length must be less then 8')


    elif check.get() == 0:
        messagebox.showinfo('error', 'please accept t&c')

    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='saloni')
            mycursor = con.cursor()

        except:
            messagebox.showinfo('error', 'database connectivity issue ')
            return
        try:
            query = 'create database driverdata'
            mycursor.execute(query)
            query = 'use driverdata'
            mycursor.execute(query)
            query = 'create table info(id int auto_increment primary key not null,email varchar(35), phone varchar(10) , username varchar(20), password varchar(20))'
            mycursor.execute(query)
        except:
            mycursor.execute('use driverdata')

        query = 'select * from info where username=%s'
        mycursor.execute(query, (usernameEntry.get()))
        row = mycursor.fetchone()
        if row != None:
            messagebox.showinfo('error', 'username already exist')
        else:
            query = 'insert into info(email,phone,username,password) values(%s,%s,%s,%s)'
            mycursor.execute(query, (emailEntry.get(),phoneEntry.get(), usernameEntry.get(), passwordEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('success', 'registration successful')
            clear()
            dsignup_window.destroy()
            import dlogin


def login_page():
    dsignup_window.destroy()
    import dlogin


def admin_page():
    dsignup_window.destroy()
    import admin


dsignup_window = Tk()
dsignup_window.configure(background='violet')
dsignup_window.geometry('1300x600')

dsignup_window.title("SINGUP PAGE ")
bgImage = ImageTk.PhotoImage(file='img5.jpg')
bgLabel = Label(dsignup_window, image=bgImage)
bgLabel.place(x=300, y=200)



frame = Frame(dsignup_window, bg='white')
frame.place(x=900, y=150)

heading = Label(frame, text='Create Account', width=15, font=('Microsoft Yahei UI Light', 23, 'bold'), bg='white',
                fg='firebrick1')
heading.grid(row=0, column=0, padx=10, pady=10)
emailLbabel = Label(frame, text='email', font=('Microsoft Yahei UI Light', 10, 'bold'), bg='white',
                    fg='firebrick1')
emailLbabel.grid(row=1, column=0, sticky='w', padx=25, pady=(10, 0))
emailEntry = Entry(frame, width=30, text='email', font=('Microsoft Yahei UI Light', 10, 'bold'), fg='white',
                   bg='firebrick1')
emailEntry.grid(row=2, column=0, sticky='w', padx=25)


phoneLbabel = Label(frame, text='phone number', font=('Microsoft Yahei UI Light', 10, 'bold'), bg='white',
                    fg='firebrick1')
phoneLbabel.grid(row=3, column=0, sticky='w', padx=25, pady=(10, 0))
phoneEntry = Entry(frame, width=30, text='ephone number', font=('Microsoft Yahei UI Light', 10, 'bold'), fg='white',
                   bg='firebrick1')
phoneEntry.grid(row=4, column=0, sticky='w', padx=25)

usernameLbabel = Label(frame, text='username', font=('Microsoft Yahei UI Light', 10, 'bold'), bg='white',
                       fg='firebrick1')
usernameLbabel.grid(row=5, column=0, sticky='w', padx=25, pady=(10, 0))
usernameEntry = Entry(frame, width=30, text='esername', font=('Microsoft Yahei UI Light', 10, 'bold'), fg='white',
                      bg='firebrick1')
usernameEntry.grid(row=6, column=0, sticky='w', padx=25)

passwordLbabel = Label(frame, text='password', font=('Microsoft Yahei UI Light', 10, 'bold'), bg='white',
                       fg='firebrick1')
passwordLbabel.grid(row=7, column=0, sticky='w', padx=25, pady=(10, 0))
passwordEntry = Entry(frame, width=30, text='password', font=('Microsoft Yahei UI Light', 10, 'bold'), fg='white',
                      bg='firebrick1')
passwordEntry.grid(row=8, column=0, sticky='w', padx=25)
openeye=PhotoImage(file='op.png')

eyeButton=Button(dsignup_window,image=openeye,bd=0,bg='white',activebackground='white',cursor='hand2',command=hide)
eyeButton.place(x=1140,y=420)

confirmLbabel = Label(frame, text='Confirm_Password', font=('Microsoft Yahei UI Light', 10, 'bold'), bg='white',
                      fg='firebrick1')
confirmLbabel.grid(row=9, column=0, sticky='w', padx=25, pady=(10, 0))
confirmEntry = Entry(frame, width=30, text='Confirm_Password', font=('Microsoft Yahei UI Light', 10, 'bold'),
                     fg='white', bg='firebrick1')
confirmEntry.grid(row=10, column=0, sticky='w', padx=25)


check = IntVar()
tandc = Checkbutton(frame, text='I agree the terms and conditions ', font=('Microsoft Yahei UI Light', 9, 'bold'),
                    bg='white', fg='firebrick1', activeforeground='firebrick1', activebackground='white',
                    cursor='hand2', variable=check)
tandc.grid(row=11, column=0, sticky='w', padx=15, pady=10)

dsignupButton = Button(frame, text='signup ', font=('Microsoft Yahei UI Light', 12, 'bold'), fg='white', bg='firebrick1',
                      activeforeground='white', activebackground='firebrick1', width=17, command=connect_database)
dsignupButton.grid(row=12, column=0, pady=10)

alredyaccount = Label(frame, text="Already have an account", font=('Microsoft Yahei UI Light', 9, 'bold'),
                      fg='firebrick1', bg='white')
alredyaccount.grid(row=13, column=0, sticky='w', padx=15, pady=10)

loginButton = Button(frame, text='login ', font=('Microsoft Yahei UI Light', 9, 'bold', 'underline'), fg='blue',
                     bg='white', bd=0, cursor='hand2', activeforeground='white', activebackground='blue',
                     command=login_page)
loginButton.place(x=170, y=470)

adminButton = Button(frame, text='admin login ', font=('Microsoft Yahei UI Light', 9, 'bold', 'underline'), fg='blue',
                     bg='white', bd=0, cursor='hand2', activeforeground='white', activebackground='blue',
                     command=admin_page)
adminButton.place(x=215, y=470)

dsignup_window.mainloop()
