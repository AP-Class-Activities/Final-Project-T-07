'''
This is a class defining a product in online shop.
You should notice that this class simpifies the product type.
Someone may add more features and bahavors to this class.


Usage:
   1) Create a new product:
        p= product(name,price,number)

   2) Print the product information:    
        print(p)

   3) Leave a comment for a product :
        a2.comments(comment)

    
'''

from random import seed
from random import randint

class Product():
    def __init__(self , name_of_product , price , num ):
        self.__name_of_product = name_of_product
        self.__price_of_product = price
        if int(num) <= 0:
            raise ValueError('the number of product should be a Natural number!')
        self.__number_of_product = int(num)
        seed(1)
        for _ in range(1):
            value = randint(100000 , 999999)
            self.__product_id = "PR" + str(value)
        self.__comments = []


    #setters and getters
    @property
    def name_of_product(self):
        return self.__name_of_product

    @name_of_product.setter
    def name_of_product(self,value):
        self.__name_of_product = value

    @property
    def price_of_product(self):
        return self.__price_of_product

    @price_of_product.setter
    def price_of_product(self,value):
        self.__price_of_product = value

    @property
    def number_of_product(self):
        return self.__number_of_product

    @number_of_product.setter
    def number_of_product(self,value):
        if value <= 0:
            raise ValueError('the number of product should be a Natural number!')
        self.__number_of_product = value

    @property
    def product_id(self):
        return self.__product_id

    @product_id.setter
    def product_id(self,value):
        self.__product_id = value

    @property
    def comments(self):
        return self.__comments

    @comments.setter
    def comments(self,value):
        self.__comments = value

    def comments(self,str):   #متد مربوط به کامنت گذاشتن برای محصول
        self.__comments.append(str)
        return self.__comments


    def __str__(self):
        return 'name:{}   ID:{}   price:{}   number:{}'\
            .format(self.__name_of_product,self.__product_id,self.__price_of_product,self.__number_of_product)

'''
p=Product('story_book','42000','10')
print(p)
'''
