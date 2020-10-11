from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import gettingData

class login_user(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x750+550+200")
        self.title("Login")
        self.resizable(False,False)
        ###Frame 1 - Covers the whole area
        self.mainFrame = Frame(self, bg='yellow', relief=SUNKEN)
        self.mainFrame.pack(fill='both', expand=True)
        self.icongive = PhotoImage(file='icons/Collyers.gif')
        self.btngive = Button(self.mainFrame, padx=10, image=self.icongive, compound=LEFT)
        self.btngive.pack(side=LEFT)
        ###Label Frame 1
        self.frame1 = Frame(self.mainFrame, relief=GROOVE, borderwidth=1, bg='#73C0F4')
        self.frame1.pack(fill='both', expand=True)
        #
        self.label2 = Label(self.frame1, text='Welcome to Collyers\nTheatre Booking System', font=('arial', 13, 'bold'))
        self.label2.pack(padx=5, pady=5, side=TOP)
        #
        self.label_1_heading = Label(self.frame1)
        self.label_1_heading.config(borderwidth=0, text='Enter your Password: ', bg='#73C0F4', font=('arial', 13, 'bold'))
        self.label_1_heading.pack(anchor=W, padx=10, pady=10, side=TOP)
        self.KEY = StringVar()
        self.txtkey = Entry(self.frame1, font=('arial', 16, 'bold'), relief=SUNKEN,
                            textvariable=self.KEY, bd=5, insertwidth=4, bg="powder blue", justify='right')
        self.txtkey.config(show='*')
        self.txtkey.pack(padx=10, pady=10)
        Btn = Button(self.frame1, text="Enter", width=10, command=self.password_check)
        Btn.pack(side=RIGHT, padx=10, pady=10)


    def password_check(self):
        userEntry = self.txtkey.get()
        mypassword = 'Pass'
        looping = False
        while looping == False:
            if userEntry == mypassword:
                self.txtkey.delete(first=0, last=END)
                gettingData.Main()

                looping = True
                return True

            else:
                self.txtkey.delete(first=0, last=END)
                messagebox.showerror("Error", 'Invalid Password')
                looping = True