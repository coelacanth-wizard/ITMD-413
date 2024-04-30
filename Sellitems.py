def priceList():
    list=[]
    add = True
    while add:
        x = float(input('Enter a price: '))
        if x == -1:
            add = False
        else: 
            list.append(x)
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
    
def welcome():
    print('Welcome to the price calculator! \nEnter the prices of your items below, stop adding by entering "-1"')
    list=[]
    add = True
    while add:
        x = float(input('Enter a price: '))
        if x == -1:
            add = False
        else: 
            list.append(x)
    print('\nCalculating...')
    print('-----'*3)
    receipt(lst)
    print('-----'*3)
    print('Thank you!')

welcome()