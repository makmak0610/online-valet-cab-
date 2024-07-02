from tkinter import *
from tkinter import ttk
from PIL import ImageTk

def book():
    cabs.destroy()
    import booking

def book1():
    cabs.destroy()
    import multiple

cabs=Tk()
cabs.configure(background='violet')
cabs.geometry('1300x700')


cabs.title("BOOKING PAGE ")
bgImage=ImageTk.PhotoImage(file='c.jpg')
bgLabel=Label(cabs,image=bgImage)
bgLabel.place(x=80,y=100)
heading=Label(text='Cars ',width=13,font=('Arial black',20,'bold'),bg='violet',fg='white')
heading.place(x=80,y=250)

bgImage1=ImageTk.PhotoImage(file='l.jpg')
bgLabel1=Label(cabs,image=bgImage1)
bgLabel1.place(x=480,y=100)
heading=Label(text='Luxury Cars ',width=13,font=('Arial black',20,'bold'),bg='violet',fg='white')
heading.place(x=480,y=250)

bgImage2=ImageTk.PhotoImage(file='b.jpg')
bgLabel2=Label(cabs,image=bgImage2)
bgLabel2.place(x=900,y=100)
heading=Label(text='Bikes ',width=13,font=('Arial black',20,'bold'),bg='violet',fg='white')
heading.place(x=900,y=270)
heading=Label(text=' Select cab or bike ',font=('Arial black',20,'bold'),bg='violet',fg='white')
heading.place(x=550,y=0)
list=["CARS","LUXURY CARS","BIKES"]
from_menu=ttk.Combobox(cabs,values=list,width=50,height=50,foreground='firebrick1',background='white')
from_menu.place(x=450, y=420)

book=Button(cabs,command=book,text='Single Stop ',font=('Arial black', 20,'bold '),bg='violet',fg='firebrick1',bd=0)
book.place(x=500,y=480)
book=Button(cabs,command=book1,text='Multiple Stop ',font=('Arial black', 20,'bold '),bg='violet',fg='firebrick1',bd=0)
book.place(x=500,y=550)





cabs.mainloop()