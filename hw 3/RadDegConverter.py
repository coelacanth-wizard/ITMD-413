#This program takes in a number and converts it to radians or degrees depending on user input 
#Author: Gabi Bartolo
import math

# deg = r * (180/pi) 
def radToDeg(r):
    deg = r * (180/math.pi)
    return deg

# rad = d * (pi/180)
def degToRad(d):
    rad = d * (math.pi/180)
    return rad

def converter():
    print("Welcome to the Radian/Degree unit converter!")
    run = True
    while run: 
        x = input("\nAre you converting to 'Rad' or 'Deg'?\n").lower()
        y = eval(input("Great! What number are you converting?\n"))
        if x == 'deg':
            print('Your Rad to Deg convesion is:',y,' = ', radToDeg(y))
        elif x == 'rad':
            print('Your Deg to Rad convesion is:',y,' = ', degToRad(y))
        else:
            print('Something went wrong, try again!')    

        r = input("\nRun converter again? <y/n>").lower()
        if r == "n":
            print('\nGoodbye!')
            run = False

# This program calculates retail prices.
# rewrite with at least two functions

mark_up = 2.5 # The markup percentage
 # Variable to control the loop.

def retailPrice(w):
     retail = w * mark_up
     return retail

def whole2Retail():
    wholesale = float(input("\nEnter the item's wholesale cost: "))
    # Validate the wholesale cost.
    while wholesale < 0:
        print('ERROR: the cost cannot be negative.')
        wholesale = float(input('Enter the correct wholesale cost:'))
    # Calculate and display the retail price.
    print('Retail price: $', format(retailPrice(wholesale), ',.2f'))

def retailCalculator():
    another = 'y'
    # Process one or more items.
    while another == 'y' or another == 'Y':
        # Get the item's wholesale cost.
        whole2Retail()
        # Do this again?
        another = input('Do you have another item? <y/n>: ')

def main():
    converter()
    retailCalculator()
    exit

def priceList():
    list=[]
    add = True
    while add:
        num = input("Enter the cost of an item:")
        try: 
            val = int(num)
        except ValueError:
            try:
                val = float(num)
            except:
                print("Invalid input, try again.")
        if val == -1:
            add = False
        else: 
            list.append(val)
    return list

def receipt(list):
    print("Price list: ")
    for i in range(len(list)): #list item prices
        print(list[i])
    subtotal = sum(list)
    taxTotal = .07 * subtotal
    print('Subtotal: $', format(subtotal, ',.2f'))
    print('Tax: $', format(taxTotal, ',.2f'))
    print('Total Price: $', format(taxTotal+subtotal, ',.2f'))  
    
def sellingItems():
    print('Welcome to the price calculator! \nEnter the prices of your items below, stop adding by entering "-1"')
    lst = priceList()
    print('\nCalculating...')
    print('-----'*3)
    receipt(lst)
    print('-----'*3)
    print('Thank you!')

def makeMatrix():
    mat = [[0,0,0],[0,0,0],[0,0,0]]
    for x in range(0,3):  #iterate through the matrix row by row
        for y in range(0,3):  #iterate through the row column by column 
            num = input("Enter a matrix value: ") 
            try: #check that the inputted value is a valid number 
                val = float(num)
            except ValueError:
                try:
                    val = int(num)
                except:
                    print("Invalid input, try again.")
            mat[x][y] = val #add number to the matrix
        print('Row ',x+1,'complete.')
    print('Matrix complete.')
    return mat
    
def multiplyMatrix(a,b):
    multiMat = [[0,0,0],[0,0,0],[0,0,0]]
    for x in range(0,3):
        for y in range(0,3):
            for z in range(0,3):
                multiMat[x][y] += a[x][z] * b[z][y]
    return multiMat

def displayMat(a,b,c): #assuming they're 3x3 matrices
    print("Multiplication Results: ")
    print(a[0][0:3],"\t\t",b[0][0:3],"\t\t",c[0][0:3])
    print(a[1][0:3],"\t*\t",b[1][0:3],"\t=\t",c[1][0:3])
    print(a[2][0:3],"\t\t",b[2][0:3],"\t\t",c[2][0:3])
    
    
