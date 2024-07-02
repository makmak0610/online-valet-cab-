from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql
import re
import datetime

def logout():
    driver_window.destroy()


def driver():
    if username.get()=='' or amount1.get()=='':
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

        query='select * from info where username=%s '
        mycursor.execute(query,(username.get()))
        row = mycursor.fetchone()
        if row == None:
            messagebox.showerror('error','invalid ')
        else:
            query = 'insert into earn(username,date,ride,earning) values(%s,%s,%s,%s)'
            mycursor.execute(query, (username.get(),a.get(), amount1.get(),  bill.get()))
            con.commit()
            con.close()
            messagebox.showinfo('done', 'thank you')
            driver_window.destroy()
            import wlcome





driver_window = Tk()
driver_window.configure(background='violet')
driver_window.geometry('1300x600')

driver_window.title("SINGUP PAGE ")
bgImage = ImageTk.PhotoImage(file='img5.jpg')
bgLabel = Label(driver_window, image=bgImage)
bgLabel.place(x=300, y=200)


def cal():
    numeric_part = re.findall(r'\d+', amount1.get())  # This pattern captures numbers with int points
    if numeric_part:
        amount = int(amount1.get())  # Convert the float to an integer
        b = amount * 80
        bill.set(b)


bill = StringVar()
Label(driver_window, text=" AMOUNT TO PAY :", bg="firebrick1").place(x=950, y=480)
Label(driver_window, text="", textvariable=bill, bg="firebrick1").place(x=1080, y=480)


a=StringVar()
current_time = datetime.datetime.now().strftime("%A,%B %d,%Y   %I:%M %p")
a.set(current_time)
date1 = Label(driver_window,textvariable=a, font="Calibri,10",bg='white').place(x=950,y=120)



heading=Label(text=' Today Earning ',font=('Arial black',30,'bold'),bg='violet',fg='firebrick1')
heading.place(x=850,y=180)

heading1=Label(text='Username',font=('Arial black',15,'bold'),bg='violet',fg='firebrick1')
heading1.place(x=850,y=280)

username = Entry(driver_window,font=('arial',15,'bold'))
username.place(x=1010, y=280)

heading1=Label(text=' No Of Rides ',font=('Arial black',15,'bold'),bg='violet',fg='firebrick1')
heading1.place(x=850,y=380)

amount1 = Entry(driver_window,font=('arial',15,'bold'))
amount1.place(x=1010, y=380)

logout=Button(driver_window,text=' LOGOUT ',font=('Arial black', 12,'bold  '),bg='violet',fg='white',command=logout,bd=0)
logout.place(x=1270,y=0)

loginButton=Button(text=' Calculate ',command=cal,font=('Arial black',15,'bold'),fg='firebrick1',bg='violet',bd=0,cursor='hand2',activeforeground='white',activebackground='pink')
loginButton.place(x=960,y=420)

loginButton=Button(text='submit',command=driver,font=('Arial black',15,'bold'),fg='firebrick1',bg='violet',bd=0,cursor='hand2',activeforeground='white',activebackground='pink')
loginButton.place(x=960,y=500)

driver_window.mainloop()