'''
This is a class defining a client and his/her wallet in a store.
Someone may add more features and bahavors to this class.


Usage:
   1) Create a new client and his/her personal wallet:
        a1=client(client full_name,client national_ID,client password,client phone_number,client address,client distance from central_warehouse)

   2) Print the client full_Information:    
        print(a1)

   3) Charging client wallet:
                  از آنجایی که به بانک اطلاعاتی }
                  جهت بررسی درست بودن شماره حساب بانکی و رمز دوم
                  دسترسی نداریم , شماره حساب بانکی
                  33 و رمز دومی که بصورت پیش فرض در خط 
                  { تعریف شده را در نظر گرفته ایم
        a1.deposit(1234567891234567,12345,amount for charging(should be less than 5000000))

   4) Withdraw shopping_amount from personal wallet:
        a1.withdraw(sum_of_shopping)

   5) Showing the history of client wallet(include deposit and withdraw):
        a1.client_history()

'''

import time

class wallet():   #کلاس مربوط به کیف پول مشتری
    def __init__(self):   
        self.__client_balance = 0   #موجودی اولیه کیف پول صفر است
        self.__client_transaction = []
        self.__acount = [1234567891234567,12345]
    
    #setters and getters
    @property
    def client_balance(self):
        return self.__client_balance
    @client_balance.setter
    def client_balance(self,value):
        self.__client_balance = value

    @property
    def client_transaction(self):
        return self.__client_transaction
    @client_transaction.setter
    def client_transaction(self,value):
        self.__client_transaction = value

    @property
    def acount(self):
        return self.__acount
    @acount.setter
    def acount(self,value):
        self.__acount = value


    def client_deposit(self,acount_No,acount_pass,amount):#شارژ کردن کیف پول
        self.acount_No = int(acount_No)
        self.acount_pass = int(acount_pass)
        if (self.acount_No != self.acount[0]) or (self.acount_pass != self.acount[1]):
            print("شماره حساب یا رمز دوم شما نادرست است.")
        else:
            self.amount = int(amount)
            if int(amount) > 0:
                self.client_balance += int(amount)
                print("کیف پول شما با موفقیت شارژ شد ... موجودی:",self.client_balance)
                self.client_activity = dict({"عملیات:":"شارژ کیف پول" ,"زمان:":time.ctime() , "مبلغ:":int(amount) , "موجودی:":self.client_balance})
                self.client_transaction.append(self.client_activity)
            else:
                print("عملیات انجام پذیر نیست ... دوباره تلاش کنید.")
    

    def client_withdraw(self,amount):   #برداشت از کیف پول
        if self.client_balance >= amount and amount > 0:  #موجودی کافی و مبلغ خرید مقداری مثبت و انجام پذیر
            self.client_balance -= amount
            print("خرید شما با موفقیت صورت گرفت ... باقیمانده کیف پول شما:",self.client_balance)
            self.client_activity = dict({"عملیات:":"خرید" ,"زمان:":time.ctime() , "مبلغ:":int(amount) , "موجودی:":self.client_balance})
            self.client_transaction.append(self.client_activity)
            return int(amount)
        elif amount <= 0:   #مبلغ خرید منفی و انجام ناپذیر
            print("عملیات انجام پذیر نیست ... دوباره تلاش کنید.")
        else:  #موجودی ناکافی
            print("موجودی کیف پول شما کافی نیست ...ابتدا آن را شارژ کنید.")

    
    def __getitem__(self,idx): #transaction پیمایش لیست transaction که مربوط به تراکنش هاست
        return self.client_transaction[idx]
    

    def client_history(self):
        if len(self.client_transaction) == 0:
            print("تاریخچه تراکنش های شما خالی است !")
        else:
            print("تاریخچه تراکنش های شما:")
            for item in self.client_transaction:
                print("\t",item)


    def wallet_history(self): 
        return self.client_history

class client(wallet):  #کلاس مشتری
    def __init__(self,fullname,id,password,phone,address,client_distance):
        super(client,self).__init__()
        self.__client_fullname = fullname
        self.__client_password = password
        self.__client_phone = int(phone)
        self.__client_id = "CU" + id[ :6]
        self.__client_address = address
        
        if int(client_distance) < 0:
            raise ValueError('Distance should be a Natural Number !')
        self.__client_distance = int(client_distance)

    #setters and getters
    @property
    def fullname(self):
        return self.__client_fullname
    @fullname.setter
    def fullname(self,value):
        self.__client_fullname = value
    

    @property
    def password(self):
        return self.__client_password
    @password.setter
    def password(self,value):
        self.__client_password = value

   
    @property
    def phone(self):
        return self.__client_phone
    @phone.setter
    def phone(self,value):
        self.__client_phone = value

   
    @property
    def id(self):
        return self.__client_id
    @id.setter
    def id(self,value):
        self.__client_id = value


    @property
    def address(self):
        return self.__client_address
    @address.setter
    def address(self,value):
        self.__client_address = value

   
    @property
    def client_distance(self):
        return self.__client_distance
    @client_distance.setter
    def client_distance(self,value):
        if value < 0:
            raise ValueError('Distance should be a Natural Number !')
        self.__client_distance = value

    
    def __str__(self): 
        return '--------------Client Information--------------\n\n      Fullname: {}   \n      ID:{}   \n      password:{}   \n      phone: {}   \n      address:{}   \n      distance: {}   \n      wallet balance: {}   \n      client history: {}'\
            .format(self.__client_fullname,self.__client_id,self.__client_password , self.__client_phone,self.__client_address, self.__client_distance,self.client_balance,self.client_transaction)

'''
a1=client('Alireza Mahdavi','123456789','83721','09127523401','guilan university','8')
print(a1)
a1.client_deposit(1234567891234567,12345,640000)
a1.client_withdraw(420000)
a1.client_history()
'''

