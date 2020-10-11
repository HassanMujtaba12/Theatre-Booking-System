from tkinter import *
from tkinter import ttk
import time
import datetime

def home(master):

    # Frame 1
    frame1 = Frame(master, bg="white",width =900)
    frame1.pack(side= TOP, fill = X)
    label_heading = Label(frame1)
    label_heading.config(text="Collyer's Theatre Ticket Booking System", font=("Simplifica 18 bold"), bg='white', padx=20, pady=25)
    label_heading.pack(side=LEFT)
    localtime = time.asctime(time.localtime(time.time()))
    lblInfo = Label(frame1, font=('arial', 12, 'bold'),
                    text=localtime, fg="Steel Blue",
                    bd=10, anchor='w',padx=50)

    lblInfo.pack(side=RIGHT)
    # Frame 2
    frame2 = Frame(master, bg="black")
    frame2.pack(side=TOP, pady=20)

    Intro = """Welcome to the Collyer's Theatre Booking System for the 2020 Collyers Performance!."""

    Intro_text = Label(frame2)
    Intro_text.config(text=Intro, font="times 12", bg="light blue")
    Intro_text.grid(row=1, padx=100, pady=10)