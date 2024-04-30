'''Create a program called store.py which contains an abstract class called Store which is made up of the following:
• Attributes/Properties
  o Store name
  o Store address
  o Store availability/status (open or closed)
  o Sales tax percentage

• Functions/Functionality
  o Constructor which provides the ability to pass and set the values for the various attributes
  o Getter and setters for all the attributes mentioned above
  o is_store_open should return True if the store is open and False if the store is closed
  o Abstract function called: calculate_total_sales_tax
  o Abstract function called calculate_total_sales
  '''
  
from abc import ABC, abstractmethod

class Store(ABC): 
    
    def __init__(self, name, address, status, salesTaxPercent):
        self.__storeName = name
        self.__storeAddress = address
        self.__storeStatus = status #open or closed
        self.__storeSalesTaxPercentage = salesTaxPercent

    @abstractmethod
    def calculate_total_sales_tax(self):
        pass
    
    @abstractmethod
    def calculate_total_sales(self):
        pass
    
    def is_Store_Open(self):
        if self.__storeStatus == 'open':
            return True
        return False
    
    '''GETTER AND SETTER METHODS'''
    @property
    def _storeName(self):
        return self.__storeName

    @_storeName.setter
    def _storeName(self, value):
        self.__storeName = value

    @property
    def _storeAddress(self):
        return self.__storeAddress

    @_storeAddress.setter
    def _storeAddress(self, value):
        self.__storeAddress = value

    @property
    def _storeStatus(self):
        return self.__storeStatus

    @_storeStatus.setter
    def _storeStatus(self, value):
        self.__storeStatus = value

    @property
    def _storeSalesTaxPercentage(self):
        return self.__storeSalesTaxPercentage

    @_storeSalesTaxPercentage.setter
    def _storeSalesTaxPercentage(self, value):
        self.__storeSalesTaxPercentage = value

    
         
    