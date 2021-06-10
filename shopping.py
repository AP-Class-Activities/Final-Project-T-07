'''
This is a class defining shopping process in online shop.
You should notice that this class simpifies the shopping type.
Someone may add more features and bahavors to this class.


Usage:
   1) Create a new cart:
        sh = Shopping(client,salesMan,product)

   2) Print the cart information:    
        print(sh)

  
'''

from client import client
from salesMan import salesMan
from product import Product

class Shopping():
    def __init__(self, client , salesMan , product ): 
          self.__client = client
          self.__salesMan = salesMan
          self.__product = product


    #setters and getters
    @property
    def client(self):
        return self.__client
     

    @client.setter
    def client(self,value): 
        self.__client = value
     

    @property
    def salesMan(self):
        return self.__salesMan
     

    @salesMan.setter
    def salesMan(self,value): 
        self.__salesMan = value
     

    @property
    def product(self):
        return self.__product
     

    @product.setter
    def product(self,value): 
        self.__product = value
    

    def delivery_distance(self,client_distance,salesman_distance):    #مجموع مسافت از انبار فروشنده تا مشتری
        self.__client_distance = client_distance
        self.__salesman_distance = salesman_distance
        self.__total_distance = self.client_distance+self.salesman_distance
        return self.total_distance


    @property
    def client_distance(self):
        return self.__client_distance

    @client_distance.setter
    def client_distance(self,value):
        self.__client_distance = value


    @property
    def salesman_distance(self):
        return self.__salesman_distance

    @salesman_distance.setter
    def salesman_distance(self,value):
        self.__salesman_distance = value
    

    @property
    def total_distance(self):
        return self.__total_distance

    @total_distance.setter
    def total_distance(self,value):
        self.__total_distance = value


    def delivery_time(self,other):   #مدت زمان ارسال کالا از انبار فروشنده تا مشتری
        total_distance = self.client_distance + other.salesman_distance
        return 3*int(total_distance)


    def sum_of_delivery_amount(self,other):  #هزینه ارسال کالا از انبار فروشنده تا مشتری
        total_distance = self.client_distance + other.salesman_distance
        return 5000*int(total_distance)


    def total_price(self,price ,total_price=None):
        total_price = price + total_price
        return total_price


    def __str__(self): 
        return 'CLIENT --> {}\n SALESMAN --> {}\n PRODUCT --> {}'\
            .format(self.client , self.salesMan , self.product)

'''
c = client('Ali Alipour','74826095','63772','09126478321','Shiraz university','32')
s = salesMan('Ashkan Samadi' , '62531' , 'Mirdamad boulevard' , '09122117558', '28736119' , '14')
p = Product('book','42000','10')
sh = Shopping(c,s,p)
print(sh)
'''

