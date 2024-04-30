'''Create a program called shopping.py which will make use of the above-mentioned
Restaurant and GroceryStore classes and call their various functions to simulate the actions
which take place in real life restaurants and grocery stores in order to test your code'''

from Restaurant import*
from Grocery_Store import*


def main():
    daifuku = Restaurant('Daifuku Ramen', '2155 S China Pl', 'open', 6.25, 15, 36, 17, 87)
    aldi = Grocery_Store('Aldi', '123 Drive', 'closed', 5.75, 'chain', 23140)
    
    print('Presenting the functions of "Restaurant" and "Grocery_Store"\n\n Restaurant: ')
    print('Name: ', daifuku._storeName())
    print('Address: ', daifuku._storeAddress())
    print('Open or Closed? ', daifuku._storeStatus())
    print('Sales tax percentage: ', daifuku.__storeSalesTaxPercentage())
    print('Price per person:', daifuku._pricePerPerson())
    print('Maximum Occupancy: ', daifuku._maxOccupancy())
    print('Current Occupancy: ', daifuku._currentOccupancy())
    print('Total People Served: ', daifuku._peopleServed())
    
    current = input('How many people is daifuku currently serving?')
    daifuku._currentlyServing(current)
    ppl = input('How many patrons would you like to seat?')
    daifuku.seatPatrons(ppl)
    ppl = input('How many patrons would you like to serve?')
    daifuku.servePatrons(ppl)
    ppl = input('How many patrons would you like to checkout?')
    daifuku.checkoutPatrons(ppl)
    
    print("Daifuku's current occupancy is: ", daifuku._currentOccupancy())
    print('Daifuku is currently serving: ', daifuku._currentlyServing())
    print('---'*7)
    
    #GROCERY STORE METHODS 
    print('Grocery Store: ')
    print('Name: ', aldi._storeName())
    print('Address: ', aldi._storeAddress())
    print('Open or Closed? ', aldi._storeStatus())
    print('Sales tax percentage: ', aldi.__storeSalesTaxPercentage())
    print('Store Type: ', aldi._storeType())
    print('Total Revenue: ', aldi._storeRevenue())
    
    num = input('How many items would you like to sell?')
    price = input('How many what price is the item?')
    aldi.sellItem(price, num)
    
main()
