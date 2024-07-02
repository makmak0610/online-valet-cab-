from tkinter import *
from PIL import ImageTk

def logout():

    about.destroy()

def welcome():
    about.destroy()
    import wlcome

def book():
    about.destroy()
    import booking


def admin_page():
    about.destroy()
    import admin

def login_page():
    about.destroy()
    import login

def signup_page():
    about.destroy()
    import signup

about=Tk()
about.configure(background='violet')
about.geometry('1300x700')


about.title("about us ")
bgImage=ImageTk.PhotoImage(file='pp.jpg')
bgLabel=Label(about,image=bgImage)
bgLabel.place(x=0,y=80)
heading=Label(about,text='Welcome  ',font=('Arial black',35,'bold'),bg='violet',fg='white')
heading.place(x=900,y=180)
heading=Label(about,text='To Pink Cabs ',font=('Arial black',35,'bold'),bg='violet',fg='white')
heading.place(x=900,y=250)
heading=Label(about,text='Started in 2024 ',font=('Arial black',35,'bold'),bg='violet',fg='white')
heading.place(x=900,y=330)
heading=Label(about,text='By Saloni',font=('Arial black',35,'bold'),bg='violet',fg='white')
heading.place(x=900,y=400)


welcome=Button(about,text='WELCOME',font=('Arial black', 12,'bold '),bg='violet',fg='white',command=welcome,bd=0)
welcome.place(x=950,y=0)

login=Button(about,text=' LOGIN ',font=('Arial black', 12,'bold '),bg='violet',fg='white',command=login_page,bd=0)
login.place(x=1050,y=0)

signup=Button(about,text=' SIGNUP ',font=('Arial black', 12,'bold  '),bg='violet',fg='white',command=signup_page,bd=0)
signup.place(x=1120,y=0)

admin=Button(about,text=' ADMIN ',font=('Arial black', 12,'bold  '),bg='violet',fg='white',command=admin_page,bd=0)
admin.place(x=1200,y=0)

logout=Button(about,text=' LOGOUT ',font=('Arial black', 12,'bold  '),bg='violet',fg='white',command=logout,bd=0)
logout.place(x=1270,y=0)

about.mainloop()