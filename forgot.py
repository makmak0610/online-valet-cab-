from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql


def hide():
    openeye.config(file='cl.png')
    password_input.config(show='*')
    eyeButton.config(command=show)


def show():
    openeye.config(file='op.png')
    password_input.config(show='')
    eyeButton.config(command=hide)




def change():
    if username_input.get() == '' or password_input.get() == '' or correctpassword_input.get()=='':
       messagebox.showerror('error', 'all field requried')
    elif password_input.get()!=correctpassword_input.get():
        messagebox.showerror('error','not matching password',parent=forgot_window)
    else:
        con = pymysql.connect(host='localhost', user='root', password='saloni',database='userdata')
        mycursor = con.cursor()
        query = 'select * from data where username=%s '
        mycursor.execute(query, (username_input.get()))
        row=mycursor.fetchone()
        if row==None:
            messagebox.showerror('error','wrong username',parent=forgot_window)
        else:
            query='update data set password=%s where username=%s'
            mycursor.execute(query,(username_input.get(),password_input.get()))
            con.commit()
            con.close()
            messagebox.showinfo('success','password set',parent=forgot_window)
            forgot_window.destroy()
            import login








forgot_window=Tk()
forgot_window.configure(background='violet')
forgot_window.geometry('1300x600')

forgot_window.title("FORGOT PASSWORD PAGE ")
bgImage=ImageTk.PhotoImage(file='img5.jpg')
bgLabel=Label(forgot_window,image=bgImage)
bgLabel.place(x=300,y=200)

heading=Label(forgot_window,text='forgot password ',width=13,font=('Microsoft Yahei UI Light',23,'bold'),bg='white',fg='firebrick1')
heading.place(x=995,y=200)

username_label = Label(forgot_window,text='Enter username',fg='firebrick1',bg='white' )
username_label.place(x=900,y=300)
username_label.config(font=('verdana',12))

username_input = Entry(forgot_window,width=20,bg='firebrick1')
username_input.place(x=1050,y=300)
username_input.config(font=('verdana',12))


password_label = Label(forgot_window,text='Enter Password',fg='firebrick1',bg='white' )
password_label.place(x=900,y=400)
password_label.config(font=('verdana',12))

password_input = Entry(forgot_window,width=20,bg='firebrick1')
password_input.place(x=1050,y=400)
password_input.config(font=('verdana',12))
openeye=PhotoImage(file='op.png')

eyeButton=Button(forgot_window,image=openeye,bd=0,bg='white',activebackground='white',cursor='hand2',command=hide)
eyeButton.place(x=1240,y=400)


correctpassword_label = Label(forgot_window,text='RE Enter Password',fg='firebrick1',bg='white' )
correctpassword_label.place(x=890,y=500)
correctpassword_label.config(font=('verdana',12))

correctpassword_input = Entry(forgot_window,width=20,bg='firebrick1')
correctpassword_input.place(x=1050,y=500)
correctpassword_input.config(font=('verdana',12))

login_btn = Button(forgot_window,text= 'Login ',fg ='firebrick1',bg='white',command=change)
login_btn.place(x=1050,y=550)
login_btn.config(font=('verdana',12))




forgot_window.mainloop()
