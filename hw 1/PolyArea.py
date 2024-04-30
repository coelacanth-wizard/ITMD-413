# Write a program that takes in the sides and length of a polygons sides and finds the area
# Author: Gabi Bartolo 

import math 

def polyArea(s, l): # s = sides, l = length of 
    ar = (s * (l**2))/(4 * math.tan(math.pi/s))
    return ar

def main():
    print('Hello and welcome to the polygon area calculator!')
    sides = eval(input('Enter a number of sides: '))
    length = eval(input('Enter the length of the sides: '))
    print('thinking...'*3)
    print('\nThe area of your polygon is: ',round(polyArea(sides, length), 4))
    
main()
