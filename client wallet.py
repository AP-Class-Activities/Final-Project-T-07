import time
'''
از آنجایی که به بانک اطلاعاتی
جهت بررسی درست بودن شماره حساب بانکی و رمز دوم
دسترسی نداریم , یک شماره حساب بانکی
و رمز دوم پیش فرض که در خط سیزدهم
تعریف شده در نظر گرفته ایم
'''
class wallet():   #کلاس مربوط به کیف پول مشتری
    def __init__(self):   
        self.balance = 0   #موجودی اولیه کیف پول صفر است
        self.transaction=[]
        self.acount=[1234567891234567,12345]
    def deposit(self,acount_No,acount_pass,amount):#شارژ کردن کیف پول
        self.acount_No=acount_No
        self.acount_pass=acount_pass
        if (self.acount_No !=self.acount[0]) or (self.acount_pass !=self.acount[1]):
            print("شماره حساب یا رمز دوم شما نادرست است.")
        else:
            self.amount=amount
            if amount > 0:
                self.balance+=amount
                print("کیف پول شما با موفقیت شارژ شد ... موجودی:",self.balance)
                self.activity=dict({"عملیات:":"شارژ کیف پول" ,"زمان:":time.ctime() ,"موجودی:":self.balance})
                self.transaction.append(self.activity)
            else:
                print("عملیات انجام پذیر نیست ... دوباره تلاش کنید.")
    def withdraw(self,amount):   #برداشت از کیف پول
        if self.balance>=amount and amount>0:  #موجودی کافی و مبلغ خرید مقداری مثبت و انجام پذیر
            self.balance-=amount
            print("خرید شما با موفقیت صورت گرفت ... باقیمانده کیف پول شما:",self.balance,)
            self.activity=dict({"عملیات:":"خرید" ,"زمان:":time.ctime() ,"موجودی:":self.balance})
            self.transaction.append(self.activity)
        elif amount<=0:   #مبلغ خرید منفی و انجام ناپذیر
            print("عملیات انجام پذیر نیست ... دوباره تلاش کنید.")
        else:  #موجودی ناکافی
            print("موجودی کیف پول شما کافی نیست ...ابتدا آن را شارژ کنید.")
    def __getitem__(self,idx): #پیمایش لیست transaction که مربوط به تراکنش هاست
        return self.transaction[idx]
    def history(self):
        if len(self.transaction)==0:
            print("تاریخچه تراکنش های شما خالی است !")
        else:
            print("تاریخچه تراکنش های شما:")
            for item in acc1.transaction:
                print("\t",item)
#main
    acc1=wallet()  #اجرای کلاس
    acount_number=int(input("شماره حساب بانکی خود را وارد کنید:"))
    acount_password=int(input("رمز دوم خود را وارد کنید:"))
    deposit_amount=int(input("مبلغ موردنظر جهت شارژ کردن کیف پول خود را وارد کنید(تومان):"))
    acc1.deposit(acount_number,acount_password,deposit_amount)
    if (acount_number==acc1.acount[0]) and (acount_password==acc1.acount[1]):
        total_shopping_amount=int(input("مبلغ پرداختی خرید خود را وارد کنید(تومان):"))
        acc1.withdraw(total_shopping_amount)
        acc1.history()