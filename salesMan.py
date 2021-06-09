'''
This is a class defining a client and his/her wallet in a store.
Someone may add more features and bahavors to this class.


Usage:
   1) Create a new salesMan :
        a2=salesMan(salesMan full_name , salesMan password , salesMan address , salesMan phoneNumber, salesMan national_ID , salesman_distancde, salesMan rate = 0)
   
   2) Print the salesMan full_Information :    
        print(a2)
   
   3) Deposit 87% of shopping amount from client wallet to salesMan wallet :
        a2.salesman_deposit(sum_of_shopping)
   
   4) Showing the history of salesMan wallet(include deposit and withdraw):
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
        self.__salesMan_distance = int(salesman_distancde)
        self.__rate = rate
        self.__salesMan_balance = 0
        self.__salesMan_transaction = []
        self.__salesMan_offcode = ['MFn6a','PSy2k','RF756','AFl76','AN9k9']

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
    def salesMan_distance(self): 
        return self.__salesMan_distance

    @salesMan_distance.setter
    def salesMan_distance(self,value): 
        if value < 1 :
            raise ValueError('distance cant be 0 or a negetive number')
        self.__salesMan_distance = value


    @property
    def rate(self): 
        return self.__rate
    
    @rate.setter
    def rate(self,value): 
        self.__rate = value


    @property
    def salesMan_balance(self):
        return self.__salesMan_balance
    @salesMan_balance.setter
    def salesMan_balance(self,value):
        self.__salesMan_balance = value


    @property
    def salesMan_transaction(self):
        return self.__salesMan_transaction
    @salesMan_transaction.setter
    def salesMan_transaction(self,value):
        self.__salesMan_transaction = value


    @property
    def salesMan_offcode(self):
        return self.__salesMan_offcode

    @salesMan_offcode.setter
    def salesMan_offcode(self,value):
        self.__salesMan_offcode = value


    def salesMan_deposit(self,amount):   #واریز 87% مبلغ خرید به کیف پول فروشنده
        if int(amount) > 0:
            self.salesMan_balance += 0.87*int(amount)
            self.salesMan_activity = dict({"عملیات:":"واریز وجه" ,"زمان:":time.ctime() , "مبلغ:":int(amount)*0.87 , "موجودی:":self.salesMan_balance})
            self.salesMan_transaction.append(self.salesMan_activity)


    def __getitem__(self,idx): #پیمایش لیست transaction که مربوط به تراکنش هاست
        return self.salesMan_transaction[idx]
    

    def salesMan_history(self):  #تاریخچه تراکنش های فروشنده
        if len(self.salesMan_transaction) == 0:
            print("تاریخچه تراکنش های شما خالی است !")
        else:
            print("تاریخچه تراکنش های شما:")
            for item in self.salesMan_transaction:
                print("\t",item)


    def salesMan_withdraw(self,acount_number,acount_password,amount):
        if (int(acount_number) == 7364526099918323) and (int(acount_password) == 34720) and (self.salesMan_balance >=  amount > 0):
            self.__salesMan_balance -= amount
            self.salesMan_activity = dict({"عملیات:":"برداشت وجه" ,"زمان:":time.ctime() , "مبلغ:":int(amount) , "موجودی:":self.salesMan_balance})
            self.salesMan_transaction.append(self.salesMan_activity)
        else:
            print("شماره حساب یا رمز دوم حساب شما صحیح نمیباشد!")


    def __str__ (self):
       return '--------------SalesMan Information--------------\n\n      Fullname:{}\n      password:{}\n      address:{}\n      phoneNumber:{}\n      ID:{}\n      distance:{}\n      rate:{}\n      Wallet Balance:{}\n      salesMan history:{}\n'\
           .format(self.fullname,self.password,self.address,self.phoneNumber,self.id,self.salesMan_distance,self.rate,self.salesMan_balance,self.salesMan_transaction)


'''
a2=salesMan("Negin Kazemi","nk5342","Guilan university","09123456789","123456789","12")
print(a2)
a2.salesMan_deposit(420000)
print(a2.salesMan_balance)
a2.salesMan_withdraw(7364526099918323,34720,250000)
print(a2.salesMan_balance)
a2.salesMan_history()
'''

