'''Create a program called restaurant.py which contains a class called Restaurant which is type
of Store. It should possess all the attributes and functions present in the Store class without
having to re-implement those in the Restaurant class. The Restaurant class is made up of the
following:

• Attributes/Properties
o Total number of people served
o Max occupancy
o Current occupancy
o Price per person

• Functions/Functionality
o Constructor which provides the ability to pass and set the values for the various
attributes
o (seat_patrons) should do the following:
  § Take the number of people to be seated as input
  § Update the values of the appropriate attributes
  § If number of people to be seated does not exceed or equals the max occupancy
   • Print “Welcome to [replace with name of restaurant]”
   • Return True
  § If number of people to be seated exceeds the max occupancy
   • Print “We are at capacity, we appreciate your patience”
   • Return False
o (serve_patrons) which should do the following:
  § Take the number of people to serve as input
  § Update the values of the appropriate attributes
  § Return the number of people being served currently
o (checkout_patrons) (this is when the patrons are ready to leave the restaurant) which should do the following:
  § Take the number of people leaving as input
  § Update the values of the appropriate attributes
  § Return the current occupancy of the restaurant
o Create a getter and setter for the attribute: Price per person'''

from Store import*

class Restaurant(Store):
  def __init__(self, name, address, status, salesTaxPercent, pricePer, maxOccu, currOccu, peopleServed):
    Store.__init__(self, name, address, status, salesTaxPercent)
    self.__currentlyServing = 0
    self.__peopleServed = peopleServed
    self.__pricePerPerson = pricePer
    self.__maxOccupancy = maxOccu
    self.__currentOccupancy = currOccu
    
  # Take the number of people to be seated as input
  # Update the values of the appropriate attributes
  def seatPatrons(self, people):
    if self.__currentOccupancy + people >= self.__maxOccupancy:
      print('We are at capacity, we appreciate your patience')
      return False
    else: 
      self.__currentOccupancy(self, people)
      print('Welcome to ', Restaurant._storeName)
      return True
    
  # Take the number of people to serve as input
  # Update the values of the appropriate attributes
  # Return the number of people being served currently
  def servePatrons(self, serving):
    self._peopleServed(self, serving)
    self._currentlyServing(self, (self._currentlyServing + serving))
    return self.__currentlyServing
  
  # this is when the patrons are ready to leave the restaurant) which should do the following:
  # Take the number of people leaving as input
  # Update the values of the appropriate attributes
  # Return the current occupancy of the restaurant
  def checkoutPatrons(self, leaving):
    self.__currentlyServing(self, (self._currentlyServing - leaving))
    self._currentOccupancy(self, (self._currentOccupancy - leaving))
    return self.__currentOccupancy
  
  def calculate_total_sales_tax(self):
    return((self.__pricePerPerson(self) * self.__peopleServed(self)) * Store.getSalesTaxPercentage(self))
    
  def calculate_total_sales(self):
    return ((self.__pricePerPerson(self) * self.__peopleServed(self)) + self.calculate_total_sales_tax(self))
    
  '''GETTER AND SETTER METHODS'''
  @property
  def _currentlyServing(self):
    return self.__currentlyServing

  @_currentlyServing.setter
  def _currentlyServing(self, value):
    self.__currentlyServing = value
    
  @property
  def _peopleServed(self):
    return self.__peopleServed

  @_peopleServed.setter
  def _peopleServed(self, value):
    self.__peopleServed = value

  @property
  def _pricePerPerson(self):
    return self.__pricePerPerson

  @_pricePerPerson.setter
  def _pricePerPerson(self, value):
    self.__pricePerPerson = value

  @property
  def _maxOccupancy(self):
    return self.__maxOccupancy

  @_maxOccupancy.setter
  def _maxOccupancy(self, value):
    self.__maxOccupancy = value

  @property
  def _currentOccupancy(self):
    return self.__currentOccupancy

  @_currentOccupancy.setter
  def _currentOccupancy(self, value):
    self.__currentOccupancy = value
