'''
This class defines a online shop. As definition,
a online shop is a collection of clients, salesMans and their product to sell.
clients can buy any products from each salesMans.
we have just one store which only operator could enter with a special ID and password.
I tried to keep the definition of this on;ine shop as simple as possible.
You can add more details as your need.

Usage:

   1) Enter as operator to store:
        St = store('admin1234','admin1234')

   2) Deposit 13% of shopping amount from client wallet to store wallet :
        St.store_deposit(sum_of_shopping)

   3) Showing the history of store wallet(include deposit):
        print(St)



'''
import time

class store():  #کلاس کیف پول فروشگاه که تنها شامل موجودی و عملیات واریز است
    def __init__(self, id , password , client = [] , salesMan = [] , product = []):   
        if (id == 'admin1234') and (password == 'admin1234') :
            self.__id = id
            self.__store_balance = 0 
            self.__store_transaction = []
            self.__clients = client
            self.__salesMans = salesMan
        else:
            raise ValueError('only operator could enter')

    @property
    def ID(self):
        return self.__id
     
    @ID.setter
    def ID(self,value): 
        self.__id = value

    @property
    def clients(self): 
        return self.__clients

    @property
    def salesMans(self): 
        return self.__salesMans


    @property
    def store_balance(self):
        return self.__store_balance

    @store_balance.setter
    def store_balance(self,value):
        self.__store_balance = value


    @property
    def store_transaction(self):
        return self.__store_transaction

    @store_transaction.setter
    def store_transaction(self,value):
        self.__store_transaction = value

    def store_deposit(self,amount):
        if int(amount) > 0:
            self.store_balance += 0.13*int(amount)
            self.store_activity = dict({"تاریخ عملیات:":time.ctime() , "مبلغ:":0.13*int(amount) , "موجودی کل:":self.store_balance})
            self.store_transaction.append(self.store_activity)
    

    def __getitem__(self,idx): #پیمایش لیست transaction که مربوط به تراکنش هاست
        return self.store_transaction[idx]


    def store_wallet_history(self):
        print("تاریخچه تراکنش های فروشگاه:")
        for item in self.__store_transaction:
            print("\t",item)


    def __str__(self):
        return self.store_wallet_history

St = store('admin1234','admin1234')
St.store_deposit(100000)
St.store_wallet_history()