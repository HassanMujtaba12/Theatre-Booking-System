from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pyodbc

connected=False
try:
    mydb = pyodbc.connect('Driver={SQL Server};'
                  'Server=svr-cmp-01;'
                  'Database=19MujtabaH48;'
                  'UID=COLLYER\19MujtabaH48;pwd=*********;'
                  'Trusted_Connection=yes;')
    cursor = mydb.cursor()
    print("connected")
    connected=True

    print ("SUCCESS")
except pyodbc.Error as err:
    print("Couldn't connect")

    
price = 0
class statistics:
    def __init__(self,master):
        global price
        self.master = master
        
        self.mainStatsFrame = Frame(self.master, bg='black')
        self.mainStatsFrame.pack(expand=True, fill='both',side=TOP)
        
        self.anotherframe = Frame(self.mainStatsFrame)
        self.anotherframe.pack(side=TOP, fill=X)
        
        self.totalStats = Frame(self.mainStatsFrame, bg='grey')
        self.totalStats.pack(side=TOP, fill='both',expand=TRUE)
        
        self.Performance1_Frame = Frame(self.anotherframe, width=333,height=300, bg='yellow')
        self.Performance1_Frame.pack(side=LEFT)
        
        self.Performance2_Frame = Frame(self.anotherframe, width=333,height=300, bg='red')
        self.Performance2_Frame.pack(side=LEFT)
        
        self.Performance3_Frame = Frame(self.anotherframe, width=333,height=300, bg='blue')
        self.Performance3_Frame.pack(side=LEFT)

        self.Perform1_Label = Label(self.Performance1_Frame, text ='Performance 1\n15/05/2020', font='arial 15 bold')
        self.Perform1_Label.place(x=80,y=10)

        self.Perform1_total_price = Label(self.Performance1_Frame, text ='Total Price:', font='arial 12 bold')
        self.Perform1_total_price.place(x=20,y=100)

        self.Perform2_Label = Label(self.Performance2_Frame, text ='Performance 2\n16/05/2020', font='arial 15 bold')
        self.Perform2_Label.place(x=80,y=10)

        self.Perform2_total_price = Label(self.Performance2_Frame, text ='Total Price:', font='arial 12 bold')
        self.Perform2_total_price.place(x=20,y=100)

        self.Perform3_Label = Label(self.Performance3_Frame, text ='Performance 3\n17/05/2020', font='arial 15 bold')
        self.Perform3_Label.place(x=80,y=10)

        self.Perform3_total_price = Label(self.Performance3_Frame, text ='Total Price:', font='arial 12 bold')
        self.Perform3_total_price.place(x=20,y=100)
        

        btngraph = Button(self.totalStats, bd = 5,
                          fg = "white", font = ('arial', 16, 'bold'),
                          width = 5, text = "Graph", bg = "#02231C",
                          command = self.graph).pack(padx=10 , pady=10, side=TOP)  

        frames = [self.Performance1_Frame,self.Performance2_Frame,self.Performance3_Frame]
        dates =  ['2020-05-15','2020-05-16','2020-05-17']

        for x in range(0,len(frames)):
            self.Calculating(frames[x],dates[x])

        self.Perform3_Label = Label(self.totalStats, text ="Total Revenue: £"+str(price)+".00", font='arial 20 bold')
        self.Perform3_Label.pack(side=LEFT)
        #print("#########price#####",price)
    def graph(self):
        label = ['Performance 1','Performance 2','Performance 3']
        index = np.arange(len(label))
        
        self.mycursor = mydb.cursor()
        sqlStatementP1= """SELECT COUNT(performance_seat.PSeatID)
                FROM performance_seat where Performance_Date=?;"""
        self.mycursor.execute(sqlStatementP1,"2020-05-15")
        TotalseatsP1 = [x[0] for x in self.mycursor.fetchall()]
        
        sqlStatementP2= """SELECT COUNT(performance_seat.PSeatID)
                FROM performance_seat where Performance_Date=?;"""
        self.mycursor.execute(sqlStatementP2,"2020-05-16")
        TotalseatsP2 = [x[0] for x in self.mycursor.fetchall()]
        
        sqlStatementP3= """SELECT COUNT(performance_seat.PSeatID)
                FROM performance_seat where Performance_Date=?;"""
        self.mycursor.execute(sqlStatementP3,"2020-05-17")
        TotalseatsP3 = [x[0] for x in self.mycursor.fetchall()]
        
        performances_data=[TotalseatsP1[0],TotalseatsP2[0],TotalseatsP3[0]]

        plt.bar(index, performances_data)
        plt.xlabel('All Performances', fontsize=10)
        plt.ylabel('No of Tickets Sold', fontsize=10)
        plt.xticks(index, label, fontsize=9)
        plt.title('Total Seats Sold per Performance')
        plt.show()

        
    def Calculating(self,frame,date):
        global price
        self.mycursor = mydb.cursor()
        sql_price = """select booking.Total_Price from booking,performance_seat
                        where booking.BookingID=performance_seat.BookingID And performance_seat.Performance_Date = ?"""
        self.mycursor.execute(sql_price,date)
        TotalPrice = [x[0] for x in self.mycursor.fetchall()]
        
        for i in range(0, len(TotalPrice)): 
            TotalPrice[i] = int(TotalPrice[i])

        Sum_of_price = sum(TotalPrice)
        price+=Sum_of_price
        
        self.priceLabel = Label(frame, text ="£"+str(Sum_of_price)+".00", font='arial 11 bold')
        self.priceLabel.place(x=120,y=100)

        sql_no_of_seats= """SELECT COUNT(performance_seat.PSeatID)
                        FROM performance_seat where Performance_Date=?;"""

        self.mycursor.execute(sql_no_of_seats,date)
        Totalseats = [x[0] for x in self.mycursor.fetchall()]
        self.seatLabel = Label(frame, text ="Total Seats: "+str(Totalseats[0]), font='arial 11 bold')
        self.seatLabel.place(x=20,y=150)

        self.remaining_seatLabel = Label(frame, text ="Remaining Seats: "+str(200-Totalseats[0]), font='arial 11 bold')
        self.remaining_seatLabel.place(x=20,y=200)
