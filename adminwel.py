
from tkinter import *

from PIL import ImageTk

def logout():
 adminwelcome1.destroy()

def mysql():
    adminwelcome1.destroy()
    import sql

def mysql7():
    adminwelcome1.destroy()
    import sql2

def dlogin_page():
    adminwelcome1.destroy()
    import dlogin

def dsignup_page():
    adminwelcome1.destroy()
    import dsignup






def mysql2():
    adminwelcome1.destroy()
    import sql3

def mysql3():
    adminwelcome1.destroy()
    import sql4

def mysql4():
    adminwelcome1.destroy()
    import sql5

def mysql5():
    adminwelcome1.destroy()
    import sql6

def welcome():
    adminwelcome1.destroy()
    import wlcome

def welcome():
    adminwelcome1.destroy()
    import wlcome


def about():
    adminwelcome1.destroy()
    import about


def admin_page():
    adminwelcome1.destroy()
    import admin

def login_page():
    adminwelcome1.destroy()
    import login

def signup_page():
    adminwelcome1.destroy()
    import signup


def mysql1():
    adminwelcome1.destroy()



def admin_page():
    adminwelcome1.destroy()
    import admin


adminwelcome1=Tk()
adminwelcome1.configure(background='violet')
adminwelcome1.geometry('1300x700')


adminwelcome1.title("Admin Welcome PAGE ")
bgImage=ImageTk.PhotoImage(file='img5.jpg')
bgLabel=Label(adminwelcome1,image=bgImage)
bgLabel.place(x=300,y=180)

heading=Label(adminwelcome1,text='Admin welcome ',font=('Arial black',25,'bold'),fg='firebrick1')
heading.place(x=900,y=180)

b=Button(adminwelcome1,text=' USERS DETAILS  ',font=('Arial black', 12,'bold  '),fg='firebrick1',command=mysql,bd=0)
b.place(x=850,y=250)
b1=Button(adminwelcome1,text='  BOOKING DETAILS (MULTIPLE STOP) ',font=('Arial black', 12,'bold  '),fg='firebrick1',command=mysql7,bd=0)
b1.place(x=850,y=300)
b2=Button(adminwelcome1,text=' BOOKING DETAILS (SINGLE STOP) ',font=('Arial black', 12,'bold  '),fg='firebrick1',command=mysql2,bd=0)
b2.place(x=850,y=350)
b3=Button(adminwelcome1,text=' PAYMENT DETAILS ',font=('Arial black', 12,'bold  '),fg='firebrick1',command=mysql3,bd=0)
b3.place(x=850,y=400)
b5=Button(adminwelcome1,text=' DRIVER DETAILS ',font=('Arial black', 12,'bold  '),fg='firebrick1',command=mysql4,bd=0)
b5.place(x=850,y=450)
b6=Button(adminwelcome1,text=' DRIVER INCOME ',font=('Arial black', 12,'bold  '),fg='firebrick1',command=mysql5,bd=0)
b6.place(x=850,y=500)




welcome=Button(adminwelcome1,text='WELCOME',font=('Arial black', 12,'bold '),bg='violet',fg='white',command=welcome,bd=0)
welcome.place(x=630,y=0)

about=Button(adminwelcome1,text='ABOUT US',font=('Arial black', 12,'bold '),bg='violet',fg='white',command=about,bd=0)
about.place(x=740,y=0)

login=Button(adminwelcome1,text=' LOGIN ',font=('Arial black', 12,'bold '),bg='violet',fg='white',command=login_page,bd=0)
login.place(x=850,y=0)

dlogin=Button(adminwelcome1,text=' DLOGIN ',font=('Arial black', 12,'bold  '),bg='violet',fg='white',command=dlogin_page,bd=0)
dlogin.place(x=930,y=0)
dsignup=Button(adminwelcome1,text=' DSIGNUP ',font=('Arial black', 12,'bold  '),bg='violet',fg='white',command=dsignup_page,bd=0)
dsignup.place(x=1019,y=0)

signup=Button(adminwelcome1,text=' SIGNUP ',font=('Arial black', 12,'bold  '),bg='violet',fg='white',command=signup_page,bd=0)
signup.place(x=1120,y=0)

admin=Button(adminwelcome1,text=' ADMIN ',font=('Arial black', 12,'bold  '),bg='violet',fg='white',command=admin_page,bd=0)
admin.place(x=1200,y=0)

logout=Button(adminwelcome1,text=' LOGOUT ',font=('Arial black', 12,'bold  '),bg='violet',fg='white',command=logout,bd=0)
logout.place(x=1270,y=0)




adminwelcome1.mainloop()