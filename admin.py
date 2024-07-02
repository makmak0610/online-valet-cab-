from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

def handle_login():
    email=email_input.get()
    password=password_input.get()

    if email =='saloni@gmail.com' and password == '1234':
        messagebox.showinfo('welcome lady boss', 'login')
        admin_window.destroy()
        import adminwel
    else:
        messagebox.showinfo('error login fail')


def hide():
    openeye.config(file='cl.png')
    password_input.config(show='*')
    eyeButton.config(command=show)


def show():
    openeye.config(file='op.png')
    password_input.config(show='')
    eyeButton.config(command=hide)





admin_window=Tk()
admin_window.configure(background='violet')
admin_window.geometry('1300x600')

admin_window.title("ADMIN PAGE ")
bgImage=ImageTk.PhotoImage(file='img5.jpg')
bgLabel=Label(admin_window,image=bgImage)
bgLabel.place(x=300,y=200)

heading=Label(admin_window,text='ADMIN LOGIN ',width=13,font=('Microsoft Yahei UI Light',23,'bold'),bg='white',fg='firebrick1')
heading.place(x=995,y=200)

email_label = Label(admin_window,text='Enter Email',fg='firebrick1',bg='white' )
email_label.place(x=920,y=300)
email_label.config(font=('verdana',12))

email_input = Entry(admin_window,width=20,bg='firebrick1')
email_input.place(x=1050,y=300)
email_input.config(font=('verdana',12))


password_label = Label(admin_window,text='Enter Password',fg='firebrick1',bg='white' )
password_label.place(x=920,y=400)
password_label.config(font=('verdana',12))

password_input = Entry(admin_window,width=20,bg='firebrick1')
password_input.place(x=1050,y=400)
password_input.config(font=('verdana',12))
openeye=PhotoImage(file='op.png')

eyeButton=Button(admin_window,image=openeye,bd=0,bg='white',activebackground='white',cursor='hand2',command=hide)
eyeButton.place(x=1250,y=400)

login_btn = Button(admin_window,text= 'Login ',fg ='firebrick1',bg='white' ,command=handle_login)
login_btn.place(x=1050,y=450)
login_btn.config(font=('verdana',12))




admin_window.mainloop()
