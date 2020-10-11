from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import Statistics
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

class management:
    def __init__(self,master):
        self.master=master
        # frames
        self.mainFrame = Frame(self.master)
        self.mainFrame.pack()

        self.centerFrame = Frame(self.mainFrame, width=1025, relief=RIDGE, bg='#e0f0f0', height=680)
        self.centerFrame.grid(row=0)

        # Center Left Frame
        self.centerLeftFrame = Frame(self.centerFrame, width=1000, height=700, bg='#e0f0f0', borderwidth=2,bd=10)
        self.centerLeftFrame.pack(side=LEFT)

        ######################################Tabs#########################################
        
        ###############tab1###############################
        self.tabs = ttk.Notebook(self.centerLeftFrame, width=1000, height=660)
        self.tabs.pack()
        self.tab1_icon = PhotoImage(file='icons/books.gif')
        self.tab2_icon = PhotoImage(file='icons/stats.gif')
        self.tab1 = ttk.Frame(self.tabs)
        self.tab2 = ttk.Frame(self.tabs)
        self.tabs.add(self.tab1, text='Management', image=self.tab1_icon, compound=LEFT)
        self.tabs.add(self.tab2, text='Statistics', image=self.tab2_icon, compound=LEFT)
        #
        Statistics.statistics(self.tab2)
        # center right frame
        centerRightFrame = Frame(self.tab1, width=150, height=800, bg='#e0f0f0', borderwidth=2, relief='sunken')
        centerRightFrame.pack(side=RIGHT,fill=Y)
        # search bar
        search_bar = LabelFrame(centerRightFrame, width=440, height=75, text='Customer Search', bg='#9bc9ff')
        search_bar.pack(fill=BOTH,side=TOP)
        self.lbl_search = Label(search_bar, text='Search (Lastname):', font='arial 12 bold', bg='#9bc9ff', fg='white')
        self.lbl_search.grid(row=0, column=0, padx=20, pady=10)
        self.ent_search = Entry(search_bar, width=20, bd=2)
        self.ent_search.grid(row=0, column=1, columnspan=3, padx=10, pady=10)
        self.btn_search = Button(search_bar, text='Search', font='arial 12', bg='#fcc324', fg='white',
                                 command=self.searching)
        self.btn_search.grid(row=1, column=3, padx=20, pady=10)

        # list bar
        list_bar = LabelFrame(centerRightFrame, width=440, height=200, text='List Box', bg='#fcc324')
        list_bar.pack(fill=BOTH,side=TOP)
        lbl_list = Label(list_bar, text='Performances', font='times 16 bold', fg='#2488ff', bg='#fcc324')
        lbl_list.grid(row=0, column=1)
        self.listChoice = IntVar()
        rb1 = Radiobutton(list_bar, text='15/05/2020', var=self.listChoice, value=1, bg='#fcc324')
        rb2 = Radiobutton(list_bar, text='16/05/2020', var=self.listChoice, value=2, bg='#fcc324')
        rb3 = Radiobutton(list_bar, text='17/05/2020', var=self.listChoice, value=3, bg='#fcc324')
        rb1.grid(row=1, column=0)
        rb2.grid(row=1, column=1)
        rb3.grid(row=1, column=2)
        btn_list_reset = Button(list_bar, text='Reset', bg='#2488ff', fg='white', font='arial 12',
                                command=self.rdBtn_Reset)
        btn_list_reset.grid(row=2, column=1, padx=40, pady=10)
        btn_list = Button(list_bar, text='Filter', bg='#2488ff', fg='white', font='arial 12',
                          command = self.searchingPerformance)
        btn_list.grid(row=2, column=2, padx=40, pady=10)
        # list books
        self.listingFrame = Frame(self.tab1,bg='#e0f0f0',width=900)
        self.listingFrame.pack(expand=True,fill='both')

        
        self.refreshBtn = Button(self.listingFrame, text='Refresh', font='arial 12', bg='#fcc324',
                                 fg='white',command=self.refreshing)
        self.refreshBtn.grid(row=10)
        #########################################################################################################################

        query_results_frame = Frame(self.listingFrame, bd=1, relief=RAISED,width=850)
        query_results_frame.grid(row=1, column=2)

        # Scrollbar
        query_scroll = Scrollbar(self.listingFrame)
        query_scroll.grid(row=0, column=1, sticky="nsew", rowspan=2)

        # Style configurations for ttk

        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"))
        style.configure("Treeview", font=("Segoe UI", 10))

        # Query output box

        self.query_box = ttk.Treeview(self.listingFrame,
                                 columns=('BookingID', 'SeatID','Lastname', 'Firstname', 'Phone',
                                          'Performance Date'),height=25,yscrollcommand=query_scroll.set)
        self.query_box["columns"] = ('BookingID', 'SeatID','Lastname', 'Firstname', 'Phone', 'Performance Date')
        self.query_box.grid(row=0, column=0)
        self.query_box.column("BookingID", width=80, anchor="center")
        self.query_box.heading("BookingID", text="BookingID")
        self.query_box.column("SeatID", width=55, anchor="center")
        self.query_box.heading("SeatID", text="SeatID")
        self.query_box.column("Lastname", width=100, anchor="center")
        self.query_box.heading("Lastname", text="Lastname")
        self.query_box.column("Firstname", width=110, anchor="center")
        self.query_box.heading("Firstname", text="Firstname")
        self.query_box.column("Phone", width=100, anchor="center")
        self.query_box.heading("Phone", text="Phone")
        self.query_box.column("Performance Date", width=160, anchor="center")
        self.query_box.heading("Performance Date", text="Performance Date")
        self.query_box["show"] = "headings"

        query_scroll.config(command=self.query_box.yview)

        self.mycursor = mydb.cursor()
        sql = """select booking.BookingID, performance_seat.SeatID, customer.Lastname,
        customer.Firstname, customer.Phone, performance_seat.Performance_Date from performance_seat
        Join booking on performance_seat.BookingID = booking.BookingID
        Join customer on booking.CustomerID = customer.CustomerID"""
        self.mycursor.execute(sql)
        mybooking = [x for x in self.mycursor.fetchall()]
        self.fullhouse = {}


        for i in range (0,len(mybooking)):
                self.fullhouse.update({mybooking[i][0]: mybooking[i]})
                self.query_box.insert('', 'end',values=(self.fullhouse[i+1][0],self.fullhouse[i+1][1],
                                                        self.fullhouse[i+1][2],self.fullhouse[i+1][3],
                                                        self.fullhouse[i+1][4],self.fullhouse[i+1][5]))
    def searching(self):
        searching_criteria = self.ent_search.get()
        self.mycursor = mydb.cursor()
        sql = """select booking.BookingID, performance_seat.SeatID, customer.Lastname, 
        customer.Firstname, customer.Phone, performance_seat.Performance_Date from performance_seat
        Join booking on performance_seat.BookingID = booking.BookingID
        Join customer on booking.CustomerID = customer.CustomerID WHERE customer.Lastname LIKE ?"""
        self.mycursor.execute(sql,("%" + searching_criteria + "%",))
        mebooking = [x for x in self.mycursor.fetchall()]
        self.house = {}
        self.query_box.delete(*self.query_box.get_children())
        for i in range(0, len(mebooking)):
            self.house.update({mebooking[i][0]: mebooking[i]})
            self.query_box.insert('', 'end',values=(mebooking[i][0],mebooking[i][1],
                                                    mebooking[i][2],mebooking[i][3],
                                                    mebooking[i][4],mebooking[i][5]))
    def refreshing(self):
        self.mycursor = mydb.cursor()
        sql = """select booking.BookingID, performance_seat.SeatID, customer.Lastname,
        customer.Firstname, customer.Phone, performance_seat.Performance_Date from performance_seat
        Join booking on performance_seat.BookingID = booking.BookingID
        Join customer on booking.CustomerID = customer.CustomerID"""
        self.mycursor.execute(sql)
        mebooking = [x for x in self.mycursor.fetchall()]
        self.house = {}

        self.query_box.delete(*self.query_box.get_children())
        for i in range(0, len(mebooking)):
            self.house.update({mebooking[i][0]: mebooking[i]})
            self.query_box.insert('', 'end',
                                  values=(mebooking[i][0],mebooking[i][1],mebooking[i][2],
                                          mebooking[i][3],mebooking[i][4],mebooking[i][5]))

    def searchingPerformance(self):
        DefaultDate = ''
        if self.listChoice.get() == 1:
            DefaultDate = '2020-05-15'
        elif self.listChoice.get() == 2:
            DefaultDate = '2020-05-16'
        elif self.listChoice.get() == 3:
            DefaultDate = '2020-05-17'

        self.mycursor = mydb.cursor()
        sqlSearchPerform = """select booking.BookingID, performance_seat.SeatID, customer.Lastname,
        customer.Firstname, customer.Phone, performance_seat.Performance_Date from performance_seat
        Join booking on performance_seat.BookingID = booking.BookingID
        Join customer on booking.CustomerID = customer.CustomerID Where performance_seat.Performance_Date=? 
        order BY customer.Lastname"""
        self.mycursor.execute(sqlSearchPerform,(DefaultDate,))
        mebooking = [x for x in self.mycursor.fetchall()]
        self.house = {}

        self.query_box.delete(*self.query_box.get_children())
        for i in range(0, len(mebooking)):
            self.house.update({mebooking[i][0]: mebooking[i]})
            self.query_box.insert('', 'end',
                                  values=(mebooking[i][0],mebooking[i][1],
                                          mebooking[i][2],mebooking[i][3],
                                          mebooking[i][4],mebooking[i][5]))

    def rdBtn_Reset(self):
        self.listChoice.set(None)
        self.searching()
