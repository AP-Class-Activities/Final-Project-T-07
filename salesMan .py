'''
This is a class defining a client and his/her wallet in a store.
Someone may add more features and bahavors to this class.


Usage:
   1) Create a new salesMan :
        a2=salesMan(salesMan full_name , salesMan address , salesMan phoneNumber, salesMan national_ID , salesman_distancde, salesMan rate = 0)
   
   2) Print the salesMan full_Information :    
        print(a2)
   
   3) Deposit 87% of shopping amount from client wallet to salesMan wallet :
        a2.salesman_deposit(sum_of_shopping)
   
   4) Showing the history of salesMan wallet(include deposit):
        a2.salesMan_history()

'''

import time

class salesMan():
    def __init__(self , fullname ,password, address , phoneNumber, id , salesman_distancde, rate = 0 ):
        self.__fullname = fullname
        self.__password = password
        self.__address = address
        self.__phoneNumber = phoneNumber
        self.__id = 'SL' + id[ :6]
        if int(salesman_distancde) < 1 :
            raise ValueError('distance cant be 0 or a negetive number')
        self.__salesman_distance = int(salesman_distancde)
        self.__rate = rate
        self.__salesman_balance = 0
        self.__salesman_transaction = []
    

    @property
    def fullname(self): 
        return self.__fullname
    @fullname.setter
    def fullname(self,value): 
        self.__fullname = value


    @property
    def password(self): 
        return self.__password
    @password.setter
    def password(self,value): 
        self.__password = value


    @property
    def address(self): 
        return self.__address
    
    @address.setter
    def address(self,value): 
        self.__address = value


    @property
    def phoneNumber(self): 
        return self.__phoneNumber

    @phoneNumber.setter
    def phoneNumber(self,value): 
        self.__phoneNumber = value


    @property
    def id(self): 
        return self.__id

    @id.setter
    def id(self,value): 
        self.__id = value
    

    @property
    def salesman_distance(self): 
        return self.__salesman_distance

    @salesman_distance.setter
    def salesman_distance(self,value): 
        if value < 1 :
            raise ValueError('distance cant be 0 or a negetive number')
        self.__salesman_distance = value


    @property
    def rate(self): 
        return self.__rate
    
    @rate.setter
    def rate(self,value): 
        self.__rate = value


    @property
    def salesman_balance(self):
        return self.__salesman_balance
    @salesman_balance.setter
    def salesman_balance(self,value):
        self.__salesman_balance = value


    @property
    def salesman_transaction(self):
        return self.__salesman_transaction
    @salesman_transaction.setter
    def salesman_transaction(self,value):
        self.__salesman_transaction = value


    def salesman_deposit(self,amount):
        if int(amount) > 0:
            self.salesman_balance += 0.87*int(amount)
            self.salesman_activity = dict({"تاریخ عملیات:":time.ctime() , "مبلغ:":0.87*int(amount) , "موجودی کل:":self.salesman_balance})
            self.salesman_transaction.append(self.salesman_activity)


    def __getitem__(self,idx): #پیمایش لیست transaction که مربوط به تراکنش هاست
        return self.salesman_transaction[idx]
    

    def salesMan_history(self):
        if len(self.salesman_transaction) == 0:
            print("تاریخچه تراکنش های شما خالی است !")
        else:
            print("تاریخچه تراکنش های شما:")
            for item in self.salesman_transaction:
                print("\t",item)


    def __str__ (self):
       return '--------------SalesMan Information--------------\n\n      Fullname:{}\n      password:{}\n      address:{}\n      phoneNumber:{}\n      ID:{}\n      distance:{}\n      rate:{}\n      Wallet Balance:{}'\
           .format(self.fullname,self.password,self.address,self.phoneNumber,self.id,self.salesman_distance,self.rate,self.salesman_balance)

'''
a2=salesMan("Parsa Shahbaz","parsa12345","Guilan university","09123456789","123456789","12")
print(a2)
a2.salesman_deposit(420000)
a2.salesMan_history()

'''


