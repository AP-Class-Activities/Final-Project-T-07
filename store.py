'''
This class defines a online shop. As definition,
a online shop is a collection of clients, salesMans and their product to sell.
clients can buy any products from each salesMans.
we have just one store which only operator could enter with a special ID(str(admin1234))
and password(str(admin1234)).
We tried to keep the definition of this online shop as simple as possible.
You can add more details as your need.

Usage:

   1) Enter as operator to store:
        St = store('admin1234','admin1234')

   2) Deposit 13% of shopping amount from client wallet to store wallet :
        St.store_deposit(sum_of_shopping)

   3) Showing the history of store wallet(include deposit):
        St.store_wallet_history()

   4) Print full information of Clients and SalesMans :
        print(St) 



'''

from salesMan import salesMan
from client import client
import pickle
import time

class store():  #کلاس کیف پول فروشگاه که تنها شامل موجودی و عملیات واریز است
    def __init__(self, id , password , client = [] , salesMan = []):   
        if (id == 'admin1234') and (password == 'admin1234') :
            self.__id = id
            self.__store_balance = 0 
            self.__store_transaction = []   #تراکنش های فروشگاه
            self.__client_file = r'data\{}_clients.dat'.format(self.__id)
            self.__salesMan_file = r'data\{}_salesMan.dat'.format(self.__id)
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
        

    def __save_clients(self): 
        with open(self.__client_file, 'wb') as file:
            pickle.dump(self.clients, file)
    
    def __read_clients(self): 
        with open(self.__client_file, 'rb') as file:
            self.__clients = pickle.load(file)

    def __save_salesMans(self): 
        with open(self.__salesMan_file, 'wb') as file:
            pickle.dump(self.salesMans, file)

    def __read_salesMans(self): 
        with open(self.__salesMan_file, 'rb') as file:
            self.__salesMans = pickle.load(file)
    
    def save_to_file(self): 
        self.__save_clients()
        self.__save_salesMans()

    def read_from_file(self): 
        self.__read_clients()
        self.__read_salesMans()


    def store_deposit(self,amount):
        if int(amount) > 0:
            self.store_balance += 0.13*int(amount)
            self.store_activity = dict({"تاریخ عملیات:":time.ctime() , "مبلغ:":0.13*int(amount) , "موجودی کل:":self.store_balance})
            self.store_transaction.append(self.store_activity)
    

    def store_wallet_history(self):
        print("تاریخچه تراکنش های فروشگاه:")
        for item in self.store_transaction:
            print("\t",item)
    
    
    def __add__(self, element): 
        if type(element) is client: 
            if element not in self.__clients:
                self.__clients.append(element)
        
        elif type(element) is salesMan: 
            if element not in self.__salesMans:
                self.__salesMans.append(element)
        
        else: 
            raise ValueError('the element you want to add should be of types [client,salesMan]')
        
        return self

    def __sub__(self, element): 
        if type(element) is client: 
            if element  in self.__clients:
                self.__clients.remove(element)
        
        elif type(element) is salesMan: 
            if element  in self.__salesMans:
                self.__salesMans.remove(element)
        
        else: 
            raise ValueError('the element you want to subtract should be of types [client,salesMan]')
        
        return self


    def __str__(self): 
        S = '\n\n==========================================================================================================\n\n'
        S += 'Store history : {}'.format(self.store_transaction)
        S += '\n\n******************************************** CLIENTS ****************************************************\n\n'
        
        for i in self.clients: 
            S += '%s\n'%(i) 
        
        S += '\n\n******************************************** SALESMANS ***************************************************\n\n'        
        for i in self.salesMans:
            S += '%s\n'%(i) 
        
        S += '========================================================================================================'
        return S


c1 = client('Ali Alipour','74826095','63772','09126478321','Shiraz university','32')
c2 = client('Nazanin Karimi','52735198','53811','09106458223','Tabriz university','19')
c3 = client('Masoud Eshraghi','23618735','19283','09356356505','Tehran university','24')

s1 = salesMan('Ashkan Samadi' , '62531' , 'Mirdamad boulevard' , '09122117558', '28736119' , '14')
s2 = salesMan('Niloufar Nasery' , '93319' ,'Pirouzi street' , '09205746404', '24639300' , '27')


St = store('admin1234','admin1234')
St = St + c1
St = St + c2
St = St + c3

St = St + s1
St = St + s2

print(St)

St.save_to_file()

St = St - c1
St = St - s1

print(St)

St.read_from_file()
print(St)
