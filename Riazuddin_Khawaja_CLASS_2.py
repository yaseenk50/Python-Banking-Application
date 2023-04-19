#not the main file, go to GUI(2) file where the code runs from
#this is for project 

class Bank(object):
    
    accountList=[] #holds all the accounts
    def display(self): #for printing purposes only, not for user
        ''' displays all the account in the accountList - not for user'''
        for account in Bank.accountList:
            print ("*********************")
            for k,v in account.options.items():
                print ('{}: {}'.format(k,v))
            print ("*********************")

    def login_validity(self, username, pin): #checks for the correct login
        ''' checks login validity using the given username and pin
        GUI file calls this method'''
        for account in Bank.accountList:
            if username == account['username'] and pin == account['pin']:
                return True
        return False

    def load_account(self,username, pin): #loads current account
        ''' loads an account if given username and pin matches
        call from GUI files'''
        for account in Bank.accountList:
            if username == account['username'] and pin == account['pin']:
                return account #account object
        return None #no object found
    
    
        
class Account(object):
    default_options = {'accountno':None,\
               'balance': 0, 'fname': None, 'lname': None, 'address1':None, \
                       'address2': None, 'username': None, 'pin': None}
    def __init__(self, **kwargs):
        self.options = Account.default_options.copy() #current object is self.options
        self.options.update(kwargs) 
        Bank.accountList.append(self) 

     

    def __getitem__(self, key): #get an item by key
        return self.options[key]
    
    def __setitem__(self, key, new_value): #set an item by key
        self.options[key] = new_value
        
    def get_balance(self, accno):
        if accno == self['accountno'] : #how to access an attribute self[key]
            return self['balance']
 
    def deposit(self, amount_to_deposit, accno):

          #add deposit amount to balance and return balance
          if accno ==self['accountno']:
              self['balance']+=float(amount_to_deposit)


        #deposits amount_to_deposit to current user

    def summary(self, accno):

        #return full name, address, account type and current balance.

        if accno ==self['accountno']:
            return self["fname"],self["lname"],self["address1"],self["address2"],self["balance"]



class Checking(Account):
    
    withdraw_charge = 1.00
    def withdraw(self, withdrawamount_to_withdraw, accno):
    
        if accno==self['accountno']:
            self['balance']-=float(withdrawamount_to_withdraw)+float(Checking.withdraw_charge)





