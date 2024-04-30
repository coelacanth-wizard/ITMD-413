#Write a program based on a flowchart for troubleshooting a diesel engine 
# Author: Gabi Bartolo 

def main():
    light = input('Check your status lights, are they: \n<1> Green\n<2> Red\n<3> Amber\n')
    if(light == '1'): # green
        print("Do restart procedure")
    elif(light == '3'): #amber
        print("Check fuel line service routine.")
    elif(light == '2'): #red    
        red()
    else:
        print("That's not a valid response...\n")
        main()

def ending():
    print("\nGoodbye!")
    return

def red():
    meter = input("Shut off all input lines and check meter #3. What is the value? \n<1> < 50 \n<2> >= 50\n")
    if(meter == '1'):
        press = input("Check the main line for test pressure. What does it read? \n<1> Normal \n<2> High \n<3> Low\n")
        if press == '1':
            print('Refer to motor service manual')
        elif press == '2' or press == '3':
            print('Refer to main line manual')
        else:
            print("That's not a valid response...\n")
            red()
    elif meter == '2':
        flow = input("Measure the flow velocity at inlet 2-B. What does it read? \n<1> Normal \n<2> High \n<3> Low\n")
        if(flow == '1'):
            print('Refer to inlet service manual')
        elif flow == '2' or flow == '3':
            print('Refer unit for factory service')
        else:
            print("That's not a valid response...\n")
            red()
    else:
        print("That's not a valid response...\n")
        red()


print("Hello and welcome to the Diesel Engine Troubleshooter!")
run = True
while(run):
    main()
    no = input('Run test again? <y/n>  ').lower()
    if(no == "n"):
        run = False 
    elif(no=="y"):
        run = True
    else:
        print("That's not a valid response...\n")
ending()
