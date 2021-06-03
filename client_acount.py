'''
Usage:
   1) Create a new client acount:
        acc1= client(client_name,client_family,client National ID Number,client age,client phone_Number,client gender,client distance from warehouse)

   2) Print the client information:    
        print(acc1)

از آنجایی که به بانک اطلاعاتی
جهت بررسی درست بودن شماره حساب بانکی و رمز دوم
دسترسی نداریم , شماره حساب بانکی
و رمز دومی که بصورت پیش فرض که در خط 22
تعریف شده را در نظر گرفته ایم

'''

import time


class wallet():   #کلاس مربوط به کیف پول مشتری
    def __init__(self):   
        self.__balance = 0   #موجودی اولیه کیف پول صفر است
        self.__transaction = []
        self.__acount = [1234567891234567,12345]
    
    #setters and getters
    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self,value):
        self.__balance = value

    @property
    def transaction(self):
        return self.__transaction
    @transaction.setter
    def transaction(self,value):
        self.__transaction = value

    @property
    def acount(self):
        return self.__acount
    @acount.setter
    def acount(self,value):
        self.__acount = value

    def deposit(self,acount_No,acount_pass,amount):#شارژ کردن کیف پول
        self.acount_No = int(acount_No)
        self.acount_pass = int(acount_pass)
        if (self.acount_No != self.acount[0]) or (self.acount_pass != self.acount[1]):
            print("شماره حساب یا رمز دوم شما نادرست است.")
        else:
            self.amount = int(amount)
            if int(amount) > 0:
                self.balance += int(amount)
                print("کیف پول شما با موفقیت شارژ شد ... موجودی:",self.balance)
                self.activity = dict({"عملیات:":"شارژ کیف پول" ,"زمان:":time.ctime() ,"موجودی:":self.balance})
                self.transaction.append(self.activity)
            else:
                print("عملیات انجام پذیر نیست ... دوباره تلاش کنید.")
    
    def withdraw(self,amount):   #برداشت از کیف پول
        if self.balance >= amount and amount > 0:  #موجودی کافی و مبلغ خرید مقداری مثبت و انجام پذیر
            self.balance -= amount
            print("خرید شما با موفقیت صورت گرفت ... باقیمانده کیف پول شما:",self.balance,)
            self.activity = dict({"عملیات:":"خرید" ,"زمان:":time.ctime() ,"موجودی:":self.balance})
            self.transaction.append(self.activity)
        elif amount <= 0:   #مبلغ خرید منفی و انجام ناپذیر
            print("عملیات انجام پذیر نیست ... دوباره تلاش کنید.")
        else:  #موجودی ناکافی
            print("موجودی کیف پول شما کافی نیست ...ابتدا آن را شارژ کنید.")
    
    def __getitem__(self,idx): #پیمایش لیست transaction که مربوط به تراکنش هاست
        return self.transaction[idx]
    
    def history(self):
        if len(self.transaction) == 0:
            print("تاریخچه تراکنش های شما خالی است !")
        else:
            print("تاریخچه تراکنش های شما:")
            for item in self.transaction:
                print("\t",item)

    def __str__(self): 
        return self.history


class client(wallet):
    def __init__(self,name,family,ID,password,age,phone,address,sex,distance):
        super().__init__()
        self.__name = name
        self.__family = family
        self.__password = password
        self.__phone = int(phone)
        self.__ID = "CU" + ID[ :6]
        self.__off_codes = []
        self.__address = address
        
        if int(age) <= 0:
            raise ValueError('age should be a Natural Number !')
        self.__age = int(age)

        if sex not in ['male', 'female']: 
            raise ValueError('the value of sex should be [male or female] ')
        self.__sex = sex
        
        if int(distance) <= 0:
            raise ValueError('Distance should be a Natural Number !')
        self.__distance = int(distance)

    #setters and getters
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        self.__name = value
    
   
    @property
    def family(self):
        return self.__family
    @family.setter
    def family(self,value):
        self.__family = value


    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self,value):
        self.__password = value

   
    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self,value):
        self.__phone = value

   
    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self,value):
        self.__ID = value


    @property
    def off_codes(self):
        return self.__off_codes
    @off_codes.setter
    def off_codes(self,value):
        self.__off_codes = value

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self,value):
        self.__address = value

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,value):
        if age<=0:
            raise ValueError('age should be a Natural Number !')
        self.__age = value

    
    @property
    def sex(self):
        return self.__sex
    @sex.setter
    def sex(self,value):
        if sex not in ['male', 'female']: 
            raise ValueError('the value of sex should be [male or female] ')
        self.__sex = value

   
    @property
    def distance(self):
        return self.__distance
    @distance.setter
    def distance(self,value):
        if distance <= 0:
            raise ValueError('Distance should be a Natural Number !')
        self.__distance = value

    
    def __str__(self): 
        return 'name: {}   family: {}   ID:{}  password:{}   age: {}   phone: {}  address:{}  sex: {}    distance: {}  balance: {}'\
            .format(self.__name,self.__family,self.__ID,self.__password, self.__age, self.__phone,self.__address, self.__sex, self.__distance,self.balance)

'''
#example client code :

a1=client('Reyhane','Farjad','123456789','rey990','19','09112345678','guilan university','female','8')
print(a1)
print(a1.balance)
a1.deposit(1234567891234567,12345,640000)
print(a1.balance)
a1.withdraw(383000)
a1.history()

'''
