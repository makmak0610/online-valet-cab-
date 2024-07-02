from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql

def cancel_user():
    if usernameEntry.get() == '':
      messagebox.showerror('error','all field requried')
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='saloni')
            mycursor = con.cursor()
        except:
            messagebox.showerror('error','not establish connection')
            return


        query = 'use userdata'
        mycursor.execute(query)

        query='select * from data where username=%s '
        mycursor.execute(query,(usernameEntry.get()))
        row = mycursor.fetchone()
        if row == None:
            messagebox.showerror('error','invalid ')
        else:
            query1='DELETE FROM data WHERE username=%s'
            mycursor.execute(query1, (usernameEntry.get()))
            con.commit()  # Commit the changes to the database
            con.close()  # Close the database connection
            cancel_window.destroy()
            import cabs






def singup_page():
    cancel_window.destroy()
    import signup

def admin_page():
    cancel_window.destroy()
    import admin


def on_enter(event):
    if usernameEntry.get()=='username':
        usernameEntry.delete(0,END)



cancel_window=Tk()
cancel_window.configure(background='violet')
cancel_window.geometry('1300x700')

cancel_window.title(" cancelL PAGE ")
bgImage=ImageTk.PhotoImage(file='img5.jpg')
bgLabel=Label(cancel_window,image=bgImage)
bgLabel.place(x=300,y=200)

heading=Label(cancel_window,text=' cancel ride  ',width=13,font=('Arial black',23,'bold'),bg='violet',fg='firebrick1')
heading.place(x=995,y=200)

usernameEntry=Entry(cancel_window,width=28,font=('Microsoft Yahei UI Light',11,'bold'),bd=0,fg='firebrick1')
usernameEntry.place(x=995,y=300)
usernameEntry.insert(0,'username')
usernameEntry.bind('<FocusIn>',on_enter)
Frame(cancel_window,width=255,height=3,bg='firebrick1').place(x=995,y=322)

cancellButton=Button(cancel_window,text='cancel',font=('Open Sans', 16,'bold'),fg='white',bg='firebrick1',bd=0,width=19,command=cancel_user)
cancellButton.place(x=995,y=480)



cancel_window.mainloop()