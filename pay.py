from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import re
import pymysql



def cancel():
    pay.destroy()
    import cancel
def valid():
    if cardEntry.get() == '' or expEntry.get() =='' or expEntry.get() == ''or cvvEntry1.get()=='' :
        messagebox.showinfo('error', 'all field required ')

    elif len(cardEntry.get()) != 12:
      messagebox.showerror('error','invaild card number ')
    elif re.match(r'^[1-9]\d{11}$',cardEntry.get()) is None:
        messagebox.showinfo('error', ' invaild card number ')
    elif re.match(r'^(0?[1-9]|1[0-2])$',expEntry.get()) is None:
        messagebox.showinfo('error', ' invaild month ')
    elif expEntry.get() > '12':
      messagebox.showerror('error', 'invaild month')
    elif re.match(r'^[1-9]\d{1}$',expEntry1.get()) is None:
        messagebox.showinfo('error', ' invaild year ')
    elif expEntry1.get() <= '24':
        messagebox.showerror('error', 'invaild year')
    elif re.match(r'^[0-9]\d{2}$',cvvEntry1.get()) is None:
        messagebox.showinfo('error', ' no cvv ')
    elif len(cvvEntry1.get()) != 3:
        messagebox.showerror('error', 'invaild CVV ')


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
        mycursor.execute(query, (usernameEntry.get()))
        row = mycursor.fetchone()
        if row == None:
            messagebox.showerror('error', 'invalid username')

        else:
            query = 'use userdata'
            mycursor.execute(query)
            query = 'insert into pay (username,card_no,exp_mon,exp_year,cvv) values(%s,%s,%s,%s,%s)'
            mycursor.execute(query, (usernameEntry.get(),cardEntry.get(), expEntry.get(), expEntry1.get(), cvvEntry1.get()))
            con.commit()
            con.close()
            messagebox.showinfo('done', 'booked ')
            pay.destroy()
            import thank



def on_enter10(event):
    if usernameEntry.get() == ' username ':
        usernameEntry.delete(0,END)



def on_enter(event):
    if cardEntry.get() == ' card number ':
        cardEntry.delete(0,END)

def on_enter1(event):
    if expEntry.get() ==' expiring mm ':
        expEntry.delete(0,END)


def on_enter2(event):
    if expEntry1.get() == ' expiring yy ':
        expEntry1.delete(0, END)


def on_enter3(event):
    if cvvEntry1.get() == ' cvv ':
        cvvEntry1.delete(0, END)



pay=Tk()
pay.configure(background='violet')
pay.geometry('1300x700')


pay.title("pay us ")
bgImage=ImageTk.PhotoImage(file='pay.jpg')
bgLabel=Label(pay,image=bgImage)
bgLabel.place(x=0,y=80)
heading=Label(pay,text='Pay ',font=('Arial black',35,'bold'),bg='violet',fg='white')
heading.place(x=1050,y=100)
usernameEntry=Entry(pay,width=28,font=('Microsoft Yahei UI Light',11,'bold'),bd=0,fg='firebrick1')
usernameEntry.place(x=1055,y=200)
usernameEntry.insert(0,' username ')
usernameEntry.bind('<FocusIn>',on_enter10)


cardEntry=Entry( pay,width=28,font=('Microsoft Yahei UI Light',11,'bold'),bd=0,fg='firebrick1')
cardEntry.place(x=1055,y=250)
cardEntry.insert(0,' card number ')
cardEntry.bind('<FocusIn>',on_enter)

expEntry=Entry(pay,width=28,font=('Microsoft Yahei UI Light',11,'bold'),bd=0,fg='firebrick1')
expEntry.place(x=1055,y=300)
expEntry.insert(0,' expiring mm ')
expEntry.bind('<FocusIn>',on_enter1)
expEntry1=Entry(pay,width=28,font=('Microsoft Yahei UI Light',11,'bold'),bd=0,fg='firebrick1')
expEntry1.place(x=1055,y=350)
expEntry1.bind('<FocusIn>',on_enter2)
expEntry1.insert(0,' expiring yy ')
cvvEntry1=Entry(pay,width=28,font=('Microsoft Yahei UI Light',11,'bold'),bd=0,fg='firebrick1')
cvvEntry1.place(x=1055,y=400)
cvvEntry1.insert(0,' cvv ')
cvvEntry1.bind('<FocusIn>',on_enter3)



submitButton=Button(pay,text=' start payment ',font=('Open Sans', 16,'bold'),fg='white',bg='firebrick1',bd=0,width=19,command=valid)
submitButton.place(x=1050,y=480)

logout=Button(pay,text=' Cancel cab ',font=('Arial black', 12,'bold  '),bg='violet',fg='white',command=cancel,bd=0)
logout.place(x=1200,y=0)

pay.mainloop()