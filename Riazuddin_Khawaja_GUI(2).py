# -------------------------------------------------------------------------------
# main file
# Final Project: Banking Application
# Name: Riazuddin Khawaja
# References: TA/professor/previous Homework Assignments
# Python Version:  3.10
#-------------------------------------------------------------------------------

from tkinter import *
from Riazuddin_Khawaja_CLASS_2 import Checking, Account, Bank
from Riazuddin_Khawaja_UTILITY import create_account_no

class MyFrame(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.bank = Bank()
        self.welcome()
 
    def clear_frame(self): #clears the previous frame
        for widget in self.winfo_children():
            widget.destroy()

    def exit_application(self):
        root.destroy()

    def logout(self):
        del self.account
        self.welcome()
        
    def welcome(self): #welcome screen
        self.clear_frame()
        
        self.welcome_label = Label(self, text = 'Welcome to 209 Banking!')
        self.welcome_label.pack()
        #create three buttons -
        self.btn1 = Button(root, text = "Existing User",command=self.existing_account_widget)
        self.btn2 = Button(root, text = "New User",command = self.new_account_widget)
        self.btn3 = Button(root, text = "Exit Application",command = self.exit_application)
        #layout  manager for label, and all buttons
        self.btn1.grid(row=2, column = 2)
        self.btn2.grid(row=3, column=2)
        self.btn3.grid(row=4, column = 2)

        
        
    def new_account_widget(self):
        
        self.clear_frame() #clears the previous frame
        #destroys previous widgets
        self.btn1.destroy() 
        self.btn2.destroy()
        self.btn3.destroy()
        
        # ********************* create widgets *********************
        label_fname = Label(self, text = "First name: ")
        self.entry_fname = Entry(self, width=15)
        label_lname = Label(self, text = "Last name: ")
        self.entry_lname = Entry(self, width=15)
        #1st label: firstname
        self.fname_label = Label(self, text = 'First Name: ')
        self.fname_label.grid(row=0, column = 0)
        #2nd label: lastname
        self.lname_label = Label(self, text = 'Last Name: ')
        self.lname_label.grid(row=1, column = 0)
        #3rd label: Address line 1
        self.address1_label = Label(self, text = 'Address line 1: ')
        self.address1_label.grid(row=2, column = 0)
         #4th label: Address line 2
        self.address2_label = Label(self, text = 'Address line 2: ')
        self.address2_label.grid(row=3, column = 0)
        #6th label: Username
        self.username_label = Label(self, text = 'Username: ')
        self.username_label.grid(row=5, column = 0)
        #7th label: PIN
        self.pin_label = Label(self, text = 'PIN: ')
        self.pin_label.grid(row=6, column = 0)
        
        
        #Text field for firstname label
        self.fname_entry = Entry(self)
        self.fname_entry.grid(row = 0, column = 1)
        #Text field for lastname field
        self.lname_entry = Entry(self)
        self.lname_entry.grid(row = 1, column = 1)
        #Text field for Address line 1
        self.address1_entry = Entry(self)
        self.address1_entry.grid(row = 2, column = 1)
        #Text field for Address line 2
        self.address2_entry = Entry(self)
        self.address2_entry.grid(row = 3, column = 1)
        #Text field for username
        self.username_entry = Entry(self)
        self.username_entry.grid(row = 5, column = 1)
        #Text field for PIN
        self.pin_entry = Entry(self)
        self.pin_entry.grid(row = 6, column = 1)
        
        
        
        
        

        #Create account button
        self.button_next = Button(self, text = "Create account", command = self.create_account_button_click)
        self.button_next.grid(row=10,column=0)
        #Main Menu button
        self.button_main_menu_title = Button(self, text = "Main Menu", command = self.welcome)
        self.button_main_menu_title.grid(row=10,column=1)







        # ********************* Layout Widgets *********************
         

    #Create account object
    def create_account_button_click(self):
        
        cfname= self.fname_entry.get()
        clname= self.lname_entry.get()
        caddress = self.address1_entry.get()
        caddress2 = self.address2_entry.get()
        cusername = self.username_entry.get()
        cpin = self.pin_entry.get()
        self.ccfname = self.fname_entry.get()



        #get() address line1, line2, username and pin


        #self.clear_frame() we do not want to clear the frame otherwise it will remove whatever information user entered
        label_accountno = Label(self, text = "Your account no: ")
        self.accountno  = StringVar(self, ' ') #create StringVar object
        label_final_accountno  = Label(self, \
                                       textvariable=self.accountno) #associate self.result with this label


        s = create_account_no()
        self.accountno.set(s) #setting the self.result label

        

        #create account object for each type of account
        d = {"fname":cfname,"lname":clname,"address1":caddress,"address2":caddress2,"username":cusername,"pin":cpin,"balance":0,"accountno":s}
        if cfname.lower()==' ':
            self.account=Checking(**d)
            print('Hello Checking!')
        else:
            self.account = Checking(**d)










        self.bank.display() #for printing purpose, not for user
        self.button_next  = Button(self, text = "Please Login Again", command=self.existing_account_widget)
        label_accountno.grid(column=0, columnspan = 2)
        label_final_accountno.grid(column=0, columnspan = 2)
        self.button_next.grid(column = 0, columnspan = 2 )\


    def existing_account_widget(self):
        self.clear_frame() #clears previous frame
        #destroys previous widgets
        self.btn1.destroy() 
        self.btn2.destroy()
        self.btn3.destroy() 
        #username label
        self.username_login_label = Label(self, text= "Username: ")
        self.username_login_label.grid(row = 0, column =0)
        #pin label
        self.pin_login_label = Label(self, text= "PIN: ")
        self.pin_login_label.grid(row = 1, column =0)


        #Text field for username_login_label
        self.username_login_entry = Entry(self)
        self.username_login_entry.grid(row=0,column=1)
        #Text field for pin_login label
        self.pin_login_entry = Entry(self)
        self.pin_login_entry.grid(row=1,column=1)




        #Create account button
        self.button_next = Button(self, text = "Login ", command = self.existing_user_options)
        self.button_next.grid(row=10,column=0)
        #Main Menu button
        self.button_main_menu_title = Button(self, text = "Main Menu", command = self.welcome)
        self.button_main_menu_title.grid(row=10,column=1)
        

        #login widget
        #username, pin: label and entry
        #login, main menu: buttons

    def login_button_click(self):
        username = self.entry_exist_username.get() #get username
        pin = self.entry_exist_pin.get() #get pin

        #check if usernmae and pin is valid using login_validity method
        self.account= self.bank.load_account(username,pin)

        if (self.bank.login_validity(username, pin)): #check validity using login_validity
            #call load_account and returns account object and
            self.bank.load_account()
           # self.account= self.bank.load_account(username,pin)
            
            #call self.existing_user_options()
            self.existing_user_options()
        else: #if invalid ask again
            self.existing_account_widget()
            

    def existing_user_options(self):
        self.clear_frame()
        self.deposit_button  = Button(self, text = "Deposit", \
                                      command=self.deposit_interface)
        self.deposit_button.grid()
        #withdraw button
        self.withdraw_button  = Button(self, text = "Withdraw", \
                                      command=self.withdraw_interface)
        self.withdraw_button.grid()
        #Account summary button
        self.accno_button  = Button(self, text = "Account Summary", \
                                      command=self.summary_interface)
        self.accno_button.grid()

        #Logout
        self.logout_button  = Button(self, text = "Logout", \
                                      command=self.welcome)
        self.logout_button.grid()

        #Exit Application
        self.exit_button  = Button(self, text = "Exit Application", \
                                      command=self.exit_application)
        self.exit_button.grid()


        
        #withdraw, summary, logout and exit application

        
    def summary_interface(self):
        self.clear_frame() #clears previous frame

        #1st label: Account Number
        self.number_label = Label(self, text = 'Account Number: ')
        self.number_label.grid(row=1, column = 0)

        
        
        #Text field for Account Number
        self.number_entry = Entry(self)
        self.number_entry.grid(row = 1, column = 1)


        
        
        
        
        

        #Create options button
        self.button_next = Button(self, text = "Options", command = self.existing_user_options)
        self.button_next.grid(row=10,column=0)
        #Main Menu button
        self.button_main_menu_title = Button(self, text = "Next", command = self.summary)
        self.button_main_menu_title.grid(row=10,column=1)

        
        
    
    def summary(self):
        self.button_next.destroy()               #destroys previous widgets
        self.button_main_menu_title.destroy()
        
        
        accno = self.number_entry.get() #obtains account no from user
        fname,lname,address,address2,balance = self.account.summary(accno)
 
        

        

        self.info_label = Label(self, text = "Account Information")

        self.info_label.grid(row=12,column=0)
        #create fname_label
        self.fname = Label(self,text=fname)
        self.fname.grid(row=13,column=0)
        #lname label
        self.lname= Label(self,text=lname)
        self.lname.grid(row=13,column=1)
          # address_label

        self.address = Label(self,text=address)
        self.address.grid(row=14,column=0)

        #address2 label
        self.address2 = Label(self,text=address2)
        self.address2.grid(row=14,column=1)

        #acctype label
       # self.acctype = Label(self,text=acctype)
        #self.acctype.grid(row=15,column=0)
        #balance label
        self.balance1 = Label(self,text=balance)
        self.balance1.grid(row=16,column=0)

        self.button_options  = Button(self, text = "Options", \
                                            command=self.existing_user_options)
        self.button_options.grid(row=20,column=1)
        
    def deposit_interface(self):
        self.clear_frame()
        #Next button will call deposit
        self.amount_label = Label(self, text = 'Amount to deposit: ')
        self.amount_label.grid(row=0, column = 0)
        #2nd label: Account Number
        self.deposit_accno_label = Label(self, text = 'Account Number: ')
        self.deposit_accno_label.grid(row=1, column = 0)

        
        
        #Text field for withdrawing
        self.deposit_amount_entry = Entry(self)
        self.deposit_amount_entry.grid(row = 0, column = 1)
        #Text field for Account Number
        self.deposit_accno_entry = Entry(self)
        self.deposit_accno_entry.grid(row = 1, column = 1)

        
        
        
        
        

        #Create account button
        self.button_next = Button(self, text = "Options", command = self.existing_user_options)
        self.button_next.grid(row=10,column=0)
        #Main Menu button
        self.button_main_menu_title = Button(self, text = "Next", command = self.deposit)
        self.button_main_menu_title.grid(row=10,column=1)

    def deposit(self):
        amount_to_deposit = self.deposit_amount_entry.get() #this should be from deposit_interface


        accno_to_deposit = self.deposit_accno_entry.get()

        self.account.deposit(amount_to_deposit, accno_to_deposit)#this one

        self.check_balance(accno_to_deposit)



        
    def withdraw_interface(self):
        self.clear_frame()



        #1st label: amount (to withdraw)
        self.amount_label = Label(self, text = 'Amount to withdraw: ')
        self.amount_label.grid(row=0, column = 0)
        #2nd label: Account Number
        self.number_label = Label(self, text = 'Account Number: ')
        self.number_label.grid(row=1, column = 0)

        
        
        #Text field for withdrawing
        self.amount_entry = Entry(self)
        self.amount_entry.grid(row = 0, column = 1)
        #Text field for Account Number
        self.number_entry = Entry(self)
        self.number_entry.grid(row = 1, column = 1)

        
        
        
        
        

        #Create account button
        self.button_next = Button(self, text = "Options", command = self.existing_user_options)
        self.button_next.grid(row=10,column=0)
        #Main Menu button

        self.button_main_menu_title = Button(self, text = "Next", command = self.withdraw)
        self.button_main_menu_title.grid(row=10,column=1)





    def withdraw(self):


        withdrawamount_to_withdraw = self.amount_entry.get() #this should be from deposit_interface
        

        withdrawaccno_to_withdraw = self.number_entry.get()

        self.account.withdraw(withdrawamount_to_withdraw, withdrawaccno_to_withdraw)#this one

        self.check_balance(withdrawaccno_to_withdraw)#and this one




        
    def check_balance(self, accno): 

        self.clear_frame()
        label_balance = Label(self, text = 'Current balance: ' + \
                              str(self.account.get_balance(accno)))
        label_balance.grid()
        
        self.options_button  = Button(self, text = "Options", \
                                            command=self.existing_user_options)
        self.options_button.grid()

#driver
root = Tk()
frame = MyFrame(root)
#frame.pack()
frame.grid()
root.mainloop()
