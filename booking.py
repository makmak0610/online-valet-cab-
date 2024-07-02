from tkinter import *
from tkinter import Entry
from tkinter import messagebox
from PIL import ImageTk
from geopy.geocoders import Nominatim
from geopy import distance
import pymysql
import re

import datetime

def reset():
    pickup_input.delete(0,END)
    drop_input.delete(0,END)

def pay():
    booking_window.destroy()
    import pay

def logout():
    booking_window.destroy()

def welcome():
    booking_window.destroy()
    import wlcome

def welcome():
    booking_window.destroy()
    import wlcome


def about():
    booking_window.destroy()
    import about


def admin_page():
    booking_window.destroy()
    import admin

def login_page():
    booking_window.destroy()
    import login

def signup_page():
    booking_window.destroy()
    import signup


def get_dis():
    try:

        geolocator = Nominatim(user_agent="geoapiExercise")
        place1 = geolocator.geocode(str(pickup_input.get()))
        place2 = geolocator.geocode(str(drop_input.get()))

        l1 = geolocator.geocode(place1)
        l2 = geolocator.geocode(place2)

        loc1 = ((l1.latitude, l1.longitude))
        loc2 = ((l2.latitude, l2.longitude))

        res = (distance.distance(loc1, loc2))

        result.set(res)
    except:
        result.set("something went wrong")
def clear():
     pickup_input.delete(0, END)
     drop_input.delete(0, END)



def connect_database():
    if pickup_input.get() == '' or drop_input.get() == '' or result.get() == '' or bill.get() == '' :
        messagebox.showerror('error', 'all fields required')

    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='saloni')
            mycursor = con.cursor()

        except:
            messagebox.showinfo('error', 'database connectivity issue ')
            return
        query = 'use userdata'
        mycursor.execute(query)
        query = 'select * from data where username=%s '
        mycursor.execute(query, (username.get()))
        row = mycursor.fetchone()
        if row == None:
            messagebox.showerror('error', 'invalid username')

        else:
            query = 'use userdata'
            mycursor.execute(query)
            query = 'insert into bd2(username,date,pickup,drop_loc,distance,bill) values(%s,%s,%s,%s,%s,%s)'
            mycursor.execute(query, (username.get(),a.get(),pickup_input.get(),drop_input.get(), result.get(), bill.get()))
            con.commit()
            con.close()
            messagebox.showinfo('done', 'booked ')
            booking_window.destroy()
            import pay






booking_window=Tk()
booking_window.configure(background='violet')
booking_window.geometry('1300x700')


booking_window.title("booking_window PAGE ")
bgImage=ImageTk.PhotoImage(file='k.webp')
bgLabel=Label(booking_window,image=bgImage)
bgLabel.place(x=0,y=100)

welcome=Button(booking_window,text='WELCOME',font=('Arial black', 12,'bold '),bg='violet',fg='white',command=welcome,bd=0)
welcome.place(x=850,y=0)

about=Button(booking_window,text='ABOUT US',font=('Arial black', 12,'bold '),bg='violet',fg='white',command=about,bd=0)
about.place(x=950,y=0)

login=Button(booking_window,text=' LOGIN ',font=('Arial black', 12,'bold '),bg='violet',fg='white',command=login_page,bd=0)
login.place(x=1050,y=0)

signup=Button(booking_window,text=' SIGNUP ',font=('Arial black', 12,'bold  '),bg='violet',fg='white',command=signup_page,bd=0)
signup.place(x=1120,y=0)

admin=Button(booking_window,text=' ADMIN ',font=('Arial black', 12,'bold  '),bg='violet',fg='white',command=admin_page,bd=0)
admin.place(x=1200,y=0)

logout=Button(booking_window,text=' LOGOUT ',font=('Arial black', 12,'bold  '),bg='violet',fg='white',command=logout,bd=0)
logout.place(x=1270,y=0)

heading=Label(text='BOOK CAB ',font=('Arial black',30,'bold'),bg='violet',fg='white')
heading.place(x=950,y=100)

username=Label(booking_window,text='Enter username ',fg='firebrick1',bg='white')
username.place(x=950,y=180)
username.config(font=('verdana',12))
username=Entry(booking_window,width=20,bg='firebrick1')
username.place(x=950,y=200)
username.config(font=('verdana',12))

pickup_label = Label(booking_window,text='Enter pickup location ',fg='firebrick1',bg='white' )
pickup_label.place(x=950,y=240)
pickup_label.config(font=('verdana',12))

pickup_input = Entry(booking_window,width=20,bg='firebrick1')
pickup_input.place(x=950,y=270)
pickup_input.config(font=('verdana',12))


drop_label = Label(booking_window,text='Enter drop location ',fg='firebrick1',bg='white' )
drop_label.place(x=950,y=320)
drop_label.config(font=('verdana',12))

drop_input = Entry(booking_window,width=20,bg='firebrick1')
drop_input.place(x=950,y=350)
drop_input.config(font=('verdana',12))


result = StringVar()
Label(booking_window, text=" Distance:",font=('verdana',12), fg='firebrick1',bg='white').place(x=950,y=440)
Label(booking_window, text="", textvariable=result, bg="firebrick1").place(x=1050,y=440)


def sum():
    numeric_part = re.findall(r'\d+\.\d+', result.get())  # This pattern captures numbers with decimal points
    if numeric_part:
        result_as_float = float(numeric_part[0])  # Convert the extracted number to a float
        result_as_int = int(result_as_float)  # Convert the float to an integer
        b = result_as_int * 0.08
        bill.set(b)

bill = StringVar()
Label(booking_window, text=" AMOUNT TO PAY :", bg="firebrick1").place(x=950,y=530)
Label(booking_window, text="", textvariable=bill, bg="firebrick1").place(x=1080,y=530)


a=StringVar()
current_time = datetime.datetime.now().strftime("%A,%B %d,%Y   %I:%M %p")
a.set(current_time)
date1 = Label(booking_window,textvariable=a, font="Calibri,10",bg='white').place(x=950,y=150)



loginButton=Button(text='Distance ',command=get_dis,font=('Arial black',15,'bold'),fg='white',bg='violet',bd=0,cursor='hand2',activeforeground='white',activebackground='pink')
loginButton.place(x=1000,y=380)
loginButton1=Button(text='Bill ',command=sum,font=('Arial black',15,'bold'),fg='white',bg='violet',bd=0,cursor='hand2',activeforeground='white',activebackground='pink')
loginButton1.place(x=1000,y=470)

reset=Button(command=reset,text='Reset',font=('arial',15,'bold'),fg='white',bg='violet',bd=0,cursor='hand2',activeforeground='white',activebackground='pink')
reset.place(x=950, y=570)
pay=Button(command=connect_database,text='PAYMENT',font=('arial',15,'bold'),fg='white',bg='violet',bd=0,cursor='hand2',activeforeground='white',activebackground='pink')
pay.place(x=1150, y=570)

booking_window.mainloop()


