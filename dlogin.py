from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql




def dlogin_user():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
      messagebox.showerror('error','all field requried')
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='saloni')
            mycursor = con.cursor()
        except:
            messagebox.showerror('error','not establish connection')
            return


        query = 'use driverdata'
        mycursor.execute(query)

        query='select * from info where username=%s and password=%s'
        mycursor.execute(query,(usernameEntry.get(),passwordEntry.get()))
        row = mycursor.fetchone()
        if row == None:
            messagebox.showerror('error','invalid ')
        else:
            dlogin_window.destroy()
            import driver




def singup_page():
    dlogin_window.destroy()
    import dsignup

def admin_page():
    dlogin_window.destroy()
    import admin



def hide():
    openeye.config(file='cl.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)


def show():
    openeye.config(file='op.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)



def on_enter(event):
    if usernameEntry.get()=='username':
        usernameEntry.delete(0,END)

def on_enter1(event):
    if passwordEntry.get()=='password':
        passwordEntry.delete(0,END)

dlogin_window=Tk()
dlogin_window.configure(background='violet')
dlogin_window.geometry('1300x700')

dlogin_window.title("dlogin PAGE ")
bgImage=ImageTk.PhotoImage(file='img5.jpg')
bgLabel=Label(dlogin_window,image=bgImage)
bgLabel.place(x=300,y=200)




heading=Label(dlogin_window,text='Driver login ',width=13,font=('Arial black',23,'bold'),bg='violet',fg='firebrick1')
heading.place(x=995,y=200)

usernameEntry=Entry(dlogin_window,width=28,font=('Microsoft Yahei UI Light',11,'bold'),bd=0,fg='firebrick1')
usernameEntry.place(x=995,y=300)
usernameEntry.insert(0,'username')
usernameEntry.bind('<FocusIn>',on_enter)
Frame(dlogin_window,width=255,height=3,bg='firebrick1').place(x=995,y=322)

passwordEntry=Entry(dlogin_window,width=28,font=('Microsoft Yahei UI Light',11,'bold'),bd=0,fg='firebrick1')
passwordEntry.place(x=995,y=360)
passwordEntry.insert(0,'password')
passwordEntry.bind('<FocusIn>',on_enter1)
Frame(dlogin_window,width=255,height=3,bg='firebrick1').place(x=995,y=382)
openeye=PhotoImage(file='op.png')

eyeButton=Button(dlogin_window,image=openeye,bd=0,bg='white',activebackground='white',cursor='hand2',command=hide)
eyeButton.place(x=1200,y=355)


dloginButton=Button(dlogin_window,text='login',font=('Open Sans', 16,'bold'),fg='white',bg='firebrick1',bd=0,width=19,command=dlogin_user)
dloginButton.place(x=995,y=480)

signupLabel=Label(dlogin_window,text='dont have an account ?',font=('Open Sans',9,'bold'),fg='firebrick1',bg='white')
signupLabel.place(x=995,y=560)


newaccountButton=Button(dlogin_window,text=' create new account ',font=('Open Sans', 9,'bold underline '),fg='blue',bg='white',activeforeground='blue',bd=0,command=singup_page)
newaccountButton.place(x=1135,y=560)

adminButton=Button(dlogin_window,text='admin login ',font=('Open Sans',9,'bold','underline'),fg='blue',bg='white',bd=0,cursor='hand2',activeforeground='white',activebackground='blue',command=admin_page)
adminButton.place(x=1135,y=590)

dlogin_window.mainloop()