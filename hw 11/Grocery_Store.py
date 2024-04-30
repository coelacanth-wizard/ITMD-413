'''Create a program called grocery_store.py which contains a class called GroceryStore which
is type of Store. It should possess all the attributes and functions present in the Store class
without having to re-implement those in the GroceryStore class. The GroceryStore class is made
up of the following:
• Attributes/Properties
  o Total revenue
  o Grocery store type (independent or chain)

• Functions/Functionality
  o Constructor which provides the ability to pass and set the values for the various attributes
  o (sell_item) which should do the following:
   § Takes the quantity and price of an item as input
   § Update the values of the appropriate attributes
   § Return the total revenue of the grocery store
  o Create a getter and setter for the attribute: Grocery Store type'''

from Store import*
  
class Grocery_Store(Store):
  def __init__(self, name, address, status, salesTaxPercent, storeType, revenue):
    Store.__init__(self, name, address, status, salesTaxPercent)
    self.__storeRevenue = revenue
    self.__storeType = storeType #independent or chain
  
  # Takes the quantity and price of an item as input
  # Update the values of the appropriate attributes
  # Return the total revenue of the grocery store
  def sellItem(self, price, amount):
    sale = price * amount
    self._storeRevenue(self, (self._storeRevenue(self) + sale))
    return self.__storeRevenue
  
  def calculate_total_sales_tax(self):
    return(Grocery_Store.getTotalRevenue(self) * Store.getSalesTaxPercentage(self))
    
  def calculate_total_sales(self):
    return(Grocery_Store.getTotalRevenue(self) + Grocery_Store.calculate_total_sales_tax(self))
  
  '''GETTER AND SETTER METHODS'''
  @property
  def _storeRevenue(self):
    return self.__storeRevenue

  @_storeRevenue.setter
  def _storeRevenue(self, value):
    self.__storeRevenue = value

  @property
  def _storeType(self):
    return self.__storeType

  @_storeType.setter
  def _storeType(self, value):
    self.__storeType = value