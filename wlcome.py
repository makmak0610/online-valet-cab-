from tkinter import *
from PIL import ImageTk

def logout():

    wlcome_window.destroy()

def about():
    wlcome_window.destroy()
    import about


def admin_page():
    wlcome_window.destroy()
    import admin

def login_page():
    wlcome_window.destroy()
    import login

def dlogin_page():
    wlcome_window.destroy()
    import dlogin

def dsignup_page():
    wlcome_window.destroy()
    import dsignup


def signup_page():
    wlcome_window.destroy()
    import signup

wlcome_window=Tk()
wlcome_window.configure(background='violet')
wlcome_window.geometry('1300x700')


wlcome_window.title("WELCOME PAGE ")
bgImage=ImageTk.PhotoImage(file='CAB.webp')
bgLabel=Label(wlcome_window,image=bgImage)
bgLabel.place(x=0,y=0)



heading=Label(wlcome_window,text='WELCOME TO PINK CABS  ',font=('Arial black',35,'bold'),bg='violet',fg='white')
heading.place(x=600,y=180)
heading2=Label(wlcome_window,text='MOVING PEOPLE ,   ',font=('Arial black',35,'bold'),bg='violet',fg='white')
heading2.place(x=680,y=290)
heading3=Label(wlcome_window,text=' AND THE WORLD  ',font=('Arial black',35,'bold'),bg='violet',fg='white')
heading3.place(x=680,y=350)




about=Button(wlcome_window,text='ABOUT US',font=('Arial black', 12,'bold '),bg='violet',fg='white',command=about,bd=0)
about.place(x=750,y=0)

login=Button(wlcome_window,text=' LOGIN ',font=('Arial black', 12,'bold '),bg='violet',fg='white',command=login_page,bd=0)
login.place(x=860,y=0)

signup=Button(wlcome_window,text=' SIGNUP ',font=('Arial black', 12,'bold  '),bg='violet',fg='white',command=signup_page,bd=0)
signup.place(x=930,y=0)

dlogin=Button(wlcome_window,text=' DLOGIN ',font=('Arial black', 12,'bold  '),bg='violet',fg='white',command=dlogin_page,bd=0)
dlogin.place(x=1020,y=0)
dsignup=Button(wlcome_window,text=' DSIGNUP ',font=('Arial black', 12,'bold  '),bg='violet',fg='white',command=dsignup_page,bd=0)
dsignup.place(x=1105,y=0)

admin=Button(wlcome_window,text=' ADMIN ',font=('Arial black', 12,'bold  '),bg='violet',fg='white',command=admin_page,bd=0)
admin.place(x=1200,y=0)

logout=Button(wlcome_window,text=' LOGOUT ',font=('Arial black', 12,'bold  '),bg='violet',fg='white',command=logout,bd=0)
logout.place(x=1270,y=0)

wlcome_window.mainloop()