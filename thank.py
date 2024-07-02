from tkinter import *
from PIL import ImageTk
import webbrowser


def welcome():
    thank.destroy()
    import wlcome

def logout():

    thank.destroy()
def callback(url):
   webbrowser.open_new_tab(url)

thank=Tk()
thank.configure(background='violet')
thank.geometry('1300x700')


thank.title("thank us ")
bgImage=ImageTk.PhotoImage(file='pp.jpg')
bgLabel=Label(thank,image=bgImage)
bgLabel.place(x=0,y=80)
heading=Label(thank,text=' Thanks ',font=('Arial black',35,'bold'),bg='violet',fg='white')
heading.place(x=900,y=180)
heading=Label(thank,text=' For Booking  ',font=('Arial black',35,'bold'),bg='violet',fg='white')
heading.place(x=850,y=250)
heading=Label(thank,text=' Feedback ',font=('Arial black',35,'bold'),bg='violet',fg='white')
heading.place(x=850,y=480)

link = Label(thank, text="Your Experience Matter ",font=('Arial black',20,'bold'),bg='violet', fg="white", cursor="hand2")
link.place(x=850,y=550)
link.bind("<Button-1>", lambda e:
callback("https://forms.gle/DcEaxnLeVnatvTsRA"))

welcome=Button(thank,text='WELCOME',font=('Arial black', 12,'bold '),bg='violet',fg='white',command=welcome,bd=0)
welcome.place(x=1150,y=0)

logout=Button(thank,text=' LOGOUT ',font=('Arial black', 12,'bold  '),bg='violet',fg='white',command=logout,bd=0)
logout.place(x=1250,y=0)
thank.mainloop()