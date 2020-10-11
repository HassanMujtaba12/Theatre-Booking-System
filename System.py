####Main Program

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import Home
import pyodbc
import string
import datetime
import Management


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


#import gettingData
#import Login
#import sys
#import Pass_Checker


class Main_Program:
    def __init__(self,master):
        self.master=master
        #Creating the GUI for the user
        self.master.configure(bg='white')
        self.master.option_add('*Font', 'Goergia 12') #font for all widgets
        self.master.option_add('*Background', 'ivory2')#background of all widgets
        self.master.option_add('*Label.Font', 'helvetica 14') #font for all labels
        self.master.geometry("1020x700+300+50")
        self.master.resizable(False,False)

        self.mainFrame=Frame(self.master)
        self.mainFrame.pack()
        #top frames
        self.topFrame= Frame(self.mainFrame,width=1025,height=700,bg='#f8f8f8',
                             padx=5,relief=SUNKEN,borderwidth=1)
        self.topFrame.pack(side=TOP,fill='both', expand = True)
##############################################################################################################################
        self.tabs= ttk.Notebook(self.topFrame,width=1025,height=700)
        ttk.Style().configure('Tab', foreground='black', background='blue')
        self.tabs.pack(expand=True)
        self.home_icon = PhotoImage(file='icons/home.gif')
        self.book_icon=PhotoImage(file='icons/book.gif')
        self.manage_icon=PhotoImage(file='icons/management.gif')
        self.book=ttk.Frame(self.tabs)
        self.manage_tab=ttk.Frame(self.tabs)
        self.home = ttk.Frame(self.tabs)
        self.booking_tabs = ttk.Notebook(self.book, width=1025, height=700)
        self.booking_tabs.pack(expand=True,side=TOP)
        self.custFormFill = ttk.Frame(self.booking_tabs,width=10, height=5)
        self.seating = ttk.Frame(self.booking_tabs)
        self.tabs.add(self.home, text='Home', image=self.home_icon, compound=LEFT)
        self.tabs.add(self.book,text='Booking',image=self.book_icon,compound=LEFT)
        self.tabs.add(self.manage_tab,text='Management',image=self.manage_icon,compound=LEFT)
        self.booking_tabs.add(self.custFormFill, text='Your Details')
        self.booking_tabs.add(self.seating, text='Select Seat',state=DISABLED)

        #Home tab
        Home.home(self.home)
        #Booking Tab
        self.Ticket_Booking(self.custFormFill)
        #Management Tab
        Management.management(self.manage_tab)

###################################################################################################################################

    def Ticket_Booking(self,master):
        ''' This function creates tkinter widgets where user can enter their data.'''
        #createWidgets(master)
        self.formFrame = Frame(master, bg='grey',width=500,height=700)
        self.formFrame.pack(fill=Y)
        self.lbl_heading = Label(self.formFrame, text="Enter Customer's Details: ", font='arial 18 bold', fg='white', bg='grey')
        self.lbl_heading.place(x=40, y=20)

        #Customer ID

        # FirstName
        self.lbl_Firstname = Label(self.formFrame, text='Firstname:', font='arial 12 bold', fg='white', bg='#fcc324',width = 11,anchor = W)
        self.lbl_Firstname.place(x=40, y=100)
        self.ent_Firstname = Entry(self.formFrame, width=29, bd=4)
        self.ent_Firstname.insert(0, 'Enter Firstname')
        self.ent_Firstname.place(x=160, y=100)
        # Lastname
        self.lbl_Lastname = Label(self.formFrame, text='Lastname :', font='arial 12 bold', fg='white', bg='#fcc324',width = 11,anchor = W)
        self.lbl_Lastname.place(x=40, y=140)
        self.ent_Lastname = Entry(self.formFrame, width=29, bd=4)
        self.ent_Lastname.insert(0, 'Enter Lastname')
        self.ent_Lastname.place(x=160, y=140)
        # Phone
        self.lbl_phone = Label(self.formFrame, text='Phone :', font='arial 12 bold', fg='white', bg='#fcc324',width = 11,anchor = W)
        self.lbl_phone.place(x=40, y=180)
        self.ent_phone = Entry(self.formFrame, width=29, bd=4)
        self.ent_phone.insert(0, 'Enter Phone Number')
        self.ent_phone.place(x=160, y=180)
        #Email
        self.lbl_Email = Label(self.formFrame, text='Email :', font='arial 12 bold', fg='white', bg='#fcc324',width = 11,anchor = W)
        self.lbl_Email.place(x=40, y=220)
        self.ent_Email = Entry(self.formFrame, width=29, bd=4)
        self.ent_Email.insert(0, 'Enter Email')
        self.ent_Email.place(x=160, y=220)
        #Customer Type
        self.lbl_CustType = Label(self.formFrame, text='Type :', font='arial 12 bold', fg='white', bg='#fcc324',width=11,anchor=W)
        self.lbl_CustType.place(x=40, y=260)
        self.ent_type = ttk.Combobox(self.formFrame,values=["Student","Teacher","Guest/Governer"],width=28, state='readonly')
        self.ent_type.place(x=160,y=260)
        self.ent_type.current(0)

        #Date
        self.lbl_Date = Label(self.formFrame, text='Performance:', font='arial 12 bold', fg='white', bg='#fcc324',width=11,anchor=W)
        self.lbl_Date.place(x=40, y=300)
        self.ent_Date = ttk.Combobox(self.formFrame,values=["2020-05-15","2020-05-16","2020-05-17"],width=28,state='readonly')
        self.ent_Date.place(x=160,y=300)
        self.ent_Date.current(0)

        #Enter Button
        self.cont_button = Button(self.formFrame, text='Continue',command = self.select_seats)
        self.cont_button.place(x=350, y=340)

#################################################################################################################################
    def select_seats(self):
        '''This function checks the data entered into the form and validates and verifies the data. IF everything is fine then it automatically enables and goes to
        seating layout page where the user can select their seats.'''

        symbols = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '"', '£', '$', '%', '^', '&', '*', '(', ')',
                   '-', '_', '+', '=', '[', ']', '{', '}', '@', ':', ';', '#', '.', '<', '>', '.', ',', '?']
        firstname_check = [item for item in list(str(self.ent_Firstname.get())) if item in symbols]
        lastname_check = [item for item in list(str(self.ent_Lastname.get())) if item in symbols]
        phone_check = [item for item in list(str(self.ent_phone.get())) if item.lower() in list(string.ascii_lowercase) or item.lower() in symbols[10:]]
        if len(firstname_check) >= 1:
            messagebox.showerror(title='Error', message=str("Please remove '" + firstname_check[0] + "' from your Firstname"))
        elif (len(self.ent_Firstname.get()) ==0) or (len(self.ent_Lastname.get()) ==0) or (len(self.ent_Email.get()) ==0):
            messagebox.showerror(title='Error', message='Please Fill in all the Entry Boxes')
        
        elif len(lastname_check) >= 1:
            messagebox.showerror(title='Error', message=str("Please remove '" + lastname_check[0] + "' from your Lastname"))
        elif len(phone_check) >= 1:
            messagebox.showerror(title='Error', message="Please remove "+str(phone_check)+" from your phone number")
        elif len(self.ent_phone.get()) != 11:
            messagebox.showerror(title='Error', message='Your Phone Number is not 11 digits')

        elif '@' not in list(str(self.ent_Email.get())):
            messagebox.showerror(title='Error', message="Your Email address isn't correct.\nPlease Add '@'!")
        else:
            self.seating_plan(self.seating)
            self.booking_tabs.tab(self.seating, state='normal')
            user = self.booking_tabs.select(self.seating)
            self.mycursor = mydb.cursor()
            sqlCust = "INSERT INTO customer (customer.Firstname, customer.Lastname, customer.Phone, customer.Email, customer.CustType) VALUES (?, ?, ?, ?,?)"
            valCust = (self.ent_Firstname.get(), self.ent_Lastname.get(), self.ent_phone.get(), self.ent_Email.get(),
                       self.ent_type.get(),)
            self.mycursor.execute(sqlCust, valCust)
            mydb.commit()

##########################################################********BOOKINGS TAB********############################################
    def seating_plan(self,master):
        '''This function creates the seat according to the performance date selected in the previous function
        and import all the seats already sold for the performance and blocks them and shows the seats for the performance date.'''
        self.regular_tickets = []
        self.reduced_tickets = []
        self.special_tickets = []
        self.blocked_tickets = []
        self.button_frame = Frame(master, bg='#d3d3d3', width=900, height=500)
        self.button_frame.pack(fill=X)
        self.stageFrame = Frame(master, bg='black')
        self.stageFrame.pack(fill='both')
        self.displayInfo = Frame(master, bg='#d3d3d3',highlightbackground="green", highlightcolor="green", highlightthickness=2)
        self.displayInfo.pack(fill='both')
        self.InstructionFrame = Frame(self.displayInfo, bg='#d3d3d3', width=500,highlightbackground="black",
                                      highlightcolor="black", highlightthickness=1)
        self.InstructionFrame.pack(side=LEFT, fill='both')
        self.ticketInfoFrame =Frame(self.displayInfo, bg = '#d3d3d3',width=500,height=500,highlightbackground="black",
                                    highlightcolor="black", highlightthickness=1)
        self.ticketInfoFrame.pack(fill='both', side = LEFT)
        self.confirmButton = Button(self.ticketInfoFrame, width=8,bg='grey', relief=GROOVE,text='Confirm',
                                    command = self.printing_index)
        self.confirmButton.place(x=350, y=100)
        self.stageLabel = Label(self.stageFrame, text='STAGE', font='arial 18 bold', fg='white', anchor=CENTER,
                                bg='black')
        self.stageLabel.pack(pady=20)
        

        self.combined = {}
        self.mycursor = mydb.cursor()
        self.mycursor.execute("SELECT performance_seat.SeatID FROM performance_seat WHERE performance_seat.SeatStatus = 1 AND performance_seat.Performance_Date = '2020-05-15'")
        self.blocked_P1 = [x[0] for x in self.mycursor.fetchall()]

        self.mycursor.execute("SELECT performance_seat.SeatID FROM performance_seat WHERE performance_seat.SeatStatus = 1 AND performance_seat.Performance_Date = '2020-05-16'")
        self.blocked_P2 = [x[0] for x in self.mycursor.fetchall()]

        self.mycursor.execute("SELECT performance_seat.SeatID FROM performance_seat WHERE performance_seat.SeatStatus = 1 AND performance_seat.Performance_Date = '2020-05-17'")
        self.blocked_P3 = [x[0] for x in self.mycursor.fetchall()]

        alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        for i in range(10):
            for j in range(20):
                seat_name = alphabet[9 - i] + str(j + 1)
                self.seat = Button(self.button_frame, width=4, height=1, text=seat_name,
                                   command=lambda f=seat_name: self.pressed(f), bg='grey', relief=GROOVE)
                self.combined.update({seat_name: self.seat})
                self.seat.grid(row=i + 3, column=j, sticky="ew", padx=2, pady=2)

                if self.ent_Date.get() == '2020-05-15':
                    if seat_name in self.blocked_P1:
                        self.combined.get(seat_name).config(bg='red')
                        self.seat.config(state='disabled')

                elif self.ent_Date.get() == '2020-05-16':
                    if seat_name in self.blocked_P2:
                        self.combined.get(seat_name).config(bg='red')
                        self.seat.config(state='disabled')

                elif self.ent_Date.get() == '2020-05-17':
                    if seat_name in self.blocked_P3:
                        self.combined.get(seat_name).config(bg='red')
                        self.seat.config(state='disabled')

        self.display_info()

#####################################################################################################################################

    def pressed(self, index):
        '''Changes the colour of the seat when clicked on, and then runs a display_info() function to show prices for the seat.'''
        self.index=index
        if self.combined.get(self.index)['bg'] == 'grey':
            self.combined.get(self.index).config(bg='white')
            self.regular_tickets.append(self.index)
            self.display_info()

        elif self.combined.get(self.index)['bg'] == 'white':
            self.combined.get(self.index).config(bg='blue')
            self.regular_tickets.remove(self.index)
            self.reduced_tickets.append(self.index)
            self.display_info()
            
        elif self.combined.get(self.index)['bg'] == 'blue':
            self.combined.get(self.index).config(bg='yellow')
            self.reduced_tickets.remove(self.index)
            self.special_tickets.append(self.index)
            self.display_info()
            
        elif self.combined.get(self.index)['bg'] == 'yellow':
            self.combined.get(self.index).config(bg='red')
            self.special_tickets.remove(self.index)
            self.blocked_tickets.append(self.index)
            self.display_info()
            
        elif self.combined.get(self.index)['bg'] == 'red':
            self.combined.get(self.index).config(bg='grey')
            self.blocked_tickets.remove(self.index)
            self.display_info()

##################################################################################################################################
    def printing_index(self):
        '''This function is ran when the 'CONFIRM' button is pressed to confirm the user's booking and then adds data to the database.
        It also then resets everything on th booking/form page to easily re-enter another'user's data.'''
        if self.total_quantity1 > 10:
            messagebox.showerror(title='Error', message='The maximum range is 10 seats. Please select less seats.')
            self.cont_button.config(state = 'disabled')
        else:
            final_list = self.regular_tickets+self.reduced_tickets+self.special_tickets
            self.mycursor = mydb.cursor()

            self.mycursor.execute("SELECT TOP 1 performance_seat.PSeatID FROM performance_seat ORDER BY performance_seat.PSeatID DESC")
            myseatresult = self.mycursor.fetchall()
            seatid = [s[0] for s in myseatresult]
            if len(seatid) >=1:
                last_seat=seatid[-1]
                for i in range(0, len(final_list)):
                    self.changes_to_database(final_list[i], (last_seat+1))
                    i += 1
                    last_seat+=1
            else:
                for i in range(0, len(final_list)):
                    self.changes_to_database(final_list[i], (i+1))
                    i += 1

            self.mycursor = mydb.cursor()
            self.mycursor.execute("SELECT performance_seat.SeatID FROM performance_seat WHERE performance_seat.SeatStatus = 1 AND performance_seat.Performance_Date = '2020-05-15'")
            self.blocked_P1 = [x[0] for x in self.mycursor.fetchall()]
            
            self.mycursor.execute("SELECT performance_seat.SeatID FROM performance_seat WHERE performance_seat.SeatStatus = 1 AND performance_seat.Performance_Date = '2020-05-16'")
            self.blocked_P2 = [x[0] for x in self.mycursor.fetchall()]
            
            self.mycursor.execute("SELECT performance_seat.SeatID FROM performance_seat WHERE performance_seat.SeatStatus = 1 AND performance_seat.Performance_Date = '2020-05-17'")
            self.blocked_P3 = [x[0] for x in self.mycursor.fetchall()]
    
    
            self.button_frame.destroy()
            self.displayInfo.destroy()
            self.stageFrame.destroy()
            self.booking_tabs.tab(self.seating,state='disabled')
            self.booking_tabs.select(self.custFormFill)
            messagebox.showinfo(title='Information', message='Data was Successfully stored!')
            self.ent_Firstname.delete(first=0, last=END)
            self.ent_Firstname.insert(0,'Enter Firstname')
            self.ent_Lastname.delete(first=0, last=END)
            self.ent_Lastname.insert(0, 'Enter Lastname')
            self.ent_phone.delete(first=0, last=END)
            self.ent_phone.insert(0, 'Enter Phone Number')
            self.ent_Email.delete(first=0, last=END)
            self.ent_Email.insert(0, 'Enter Email')
            self.ent_type.current(0)
            self.ent_Date.current(0)
            
            from Management import management
            management(self.manage_tab)


#####################################################################################################################################

    def display_info(self):
        ''' This function creates table listing the price, quantity of each type of seat and displays the total price'''
        regularTicket = 10
        reducedTicket = 5
        SpecialTicket = 0

        # displaying ticket infromation
        self.ticket_type_heading = Label(self.ticketInfoFrame)
        self.ticket_type_heading.config(text="Type", font="arial 10 bold", bg="grey",width=14, anchor=CENTER)
        self.ticket_type_heading.place(x=5, y=30)

        self.ticket_quantity_heading = Label(self.ticketInfoFrame)
        self.ticket_quantity_heading.config(text="Quantity", font="arial 10 bold", bg="grey",width=9, anchor=CENTER)
        self.ticket_quantity_heading.place(x=130, y=30)

        self.ticket_price_heading = Label(self.ticketInfoFrame)
        self.ticket_price_heading.config(text="Total Price", font="arial 10 bold", bg="grey",width=9, anchor=CENTER)
        self.ticket_price_heading.place(x=215, y=30)

        # Regular Tickets
        self.regular_tickets_text = Label(self.ticketInfoFrame)
        self.regular_tickets_text.config(text="Regular Tickets", font="arial 10 bold", bg="grey", fg="Black",anchor = W,width=14)
        self.regular_tickets_text.place(x=5, y=59)

        self.regular_tickets_price = Label(self.ticketInfoFrame)
        self.regular_tickets_price.config(text=("£"+str(len(self.regular_tickets)*regularTicket)+".00"), font="arial 10", bg="grey",width=9)
        self.regular_tickets_price.place(x=215, y=59)

        self.regular_quantity = Label(self.ticketInfoFrame)
        self.regular_quantity.config(text=len(self.regular_tickets), font="arial 10", bg="grey",width=9)
        self.regular_quantity.place(x=130, y=59)

        # Reduced Tickets
        self.reduced_tickets_text = Label(self.ticketInfoFrame)
        self.reduced_tickets_text.config(text="Reduced Tickets", font="arial 10 bold", bg="grey", fg="Black",anchor = W,width=14)
        self.reduced_tickets_text.place(x=5, y=85)

        self.reduced_tickets_price = Label(self.ticketInfoFrame)
        self.reduced_tickets_price.config(text=("£"+str(len(self.reduced_tickets)*reducedTicket)+".00"), font="arial 10", bg="grey",width=9)
        self.reduced_tickets_price.place(x=215, y=85)

        self.reduced_quantity = Label(self.ticketInfoFrame)
        self.reduced_quantity.config(text=len(self.reduced_tickets), font="arial 10", bg="grey",width=9)
        self.reduced_quantity.place(x=130, y=85)

        # Special Tickets
        self.special_tickets_text = Label(self.ticketInfoFrame)
        self.special_tickets_text.config(text="Special Tickets", font="arial 10 bold", bg="grey", fg="Black",anchor = W,width=14)
        self.special_tickets_text.place(x=5, y=111)

        self.special_tickets_price = Label(self.ticketInfoFrame)
        self.special_tickets_price.config(text=("£"+str(len(self.special_tickets)*SpecialTicket)+".00"), font="arial 10", bg="grey",width=9)
        self.special_tickets_price.place(x=215, y=111)

        self.special_quantity = Label(self.ticketInfoFrame)
        self.special_quantity.config(text=len(self.special_tickets), font="arial 10", bg="grey",width=9)
        self.special_quantity.place(x=130, y=111)

        ######### Total Tickets ##########
        self.total_tickets_text = Label(self.ticketInfoFrame)
        self.total_tickets_text.config(text="Total Tickets", font="arial 10 bold", bg="grey",anchor = W,width=14)
        self.total_tickets_text.place(x=5, y=137)

        self.total_price = (len(self.regular_tickets)*regularTicket) + (len(self.reduced_tickets)*reducedTicket) + (len(self.special_tickets)*SpecialTicket)

        self.total_tickets_price = Label(self.ticketInfoFrame)
        self.total_tickets_price.config(text=("£"+str(self.total_price)+".00"), font="arial 10 bold", bg="grey",width=9)
        self.total_tickets_price.place(x=215, y=137)

        self.total_quantity1 = len(self.regular_tickets) + len(self.reduced_tickets) + len(self.special_tickets)

        self.total_quantity = Label(self.ticketInfoFrame)
        self.total_quantity.config(text=self.total_quantity1, font="arial 10 bold", bg="grey",width=9)
        self.total_quantity.place(x=130, y=137)
        




        #########instructions##########
        self.instruction_label = Label(self.InstructionFrame)
        self.instruction_label.config(text='Instructions', font="arial 13 bold", bg="light blue",width=20)
        self.instruction_label.place(x=150, y =5)

        self.buttonRep1 = Button(self.InstructionFrame, width=4,bg='white', relief=GROOVE)
        self.buttonRep1.place(x=10, y=30)
        self.rep1_label = Label(self.InstructionFrame, text=u"\u2192")
        self.rep1_label.place(x=90, y=30)
        self.rep1_name = Label(self.InstructionFrame, text='Regular', font = 'arial 11 bold',bg='white')
        self.rep1_name.place(x=140, y = 30)

        self.buttonRep2 = Button(self.InstructionFrame, width=4,bg='blue', relief=GROOVE)
        self.buttonRep2.place(x=10, y=60)
        self.rep2_label = Label(self.InstructionFrame, text=u"\u2192")
        self.rep2_label.place(x=90, y=60)
        self.rep2_name = Label(self.InstructionFrame, text='Reduced', font = 'arial 11 bold',bg='blue')
        self.rep2_name.place(x=140, y = 60)

        self.buttonRep3 = Button(self.InstructionFrame, width=4,bg='yellow', relief=GROOVE)
        self.buttonRep3.place(x=10, y=90)
        self.rep3_label = Label(self.InstructionFrame, text=u"\u2192")
        self.rep3_label.place(x=90, y=90)
        self.rep3_name = Label(self.InstructionFrame, text='Special', font = 'arial 11 bold',bg='yellow')
        self.rep3_name.place(x=140, y = 90)

        self.buttonRep4 = Button(self.InstructionFrame, width=4,bg='red', relief=GROOVE)
        self.buttonRep4.place(x=10, y=120)
        self.rep4_label = Label(self.InstructionFrame, text=u"\u2192")
        self.rep4_label.place(x=90, y=120)
        self.rep4_name = Label(self.InstructionFrame, text='Blocked', font = 'arial 11 bold',bg='red')
        self.rep4_name.place(x=140, y = 120)

        mytext = "To book a seat:\n1) Choose a seats from above\n2) See prices in the table\n3) Click confirm to book ticket"
        self.main_instruction = Label(self.InstructionFrame,text=mytext,width=25, height=7,font='arial 11',anchor=W)
        self.main_instruction.place(x=250, y=30)

##################################################################################################################################

    def changes_to_database(self,index,count):
        '''This function adds data to the database and retrieves some values for the next booking.'''
        price=0
        if index in self.regular_tickets:
            price=10
        elif index in self.reduced_tickets:
            price=5
        else:
            price=0
        self.mycursor = mydb.cursor()
        self.mycursor.execute("SELECT TOP 1 customer.CustomerID FROM customer ORDER BY customer.CustomerID DESC")
        mycustidresult = self.mycursor.fetchall()
        custid = [s[0] for s in mycustidresult]

        sqlBook = "INSERT INTO booking (booking.BookingID,booking.CustomerID,booking.Total_Price) VALUES (?,?,?)"
        valBook = (count,custid[0],float(price))
        self.mycursor.execute(sqlBook,valBook)
        mydb.commit()

        sqlPerformSeat = '''INSERT INTO performance_seat(performance_seat.PSeatID, performance_seat.SeatID, 
        performance_seat.SeatStatus, performance_seat.Performance_Date,performance_seat.BookingID) VALUES(?,?,?,?,?)'''

        valPerformSeat = (count,index,1,self.ent_Date.get(),count,)
        self.mycursor.execute(sqlPerformSeat,valPerformSeat)
        mydb.commit()

##########################################################################################################################################################################

def main():
    root = Tk()
    app = Main_Program(root)
    root.title("Theatre Ticket Booking System")
    root.iconbitmap('icons/image.ico')
    root.mainloop()


if __name__ == '__main__':
    main()
