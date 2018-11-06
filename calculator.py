''' 
    Python Project: Magical calculator
    Author: Jegede Ayodeji
    Inspired by: The Complete Python 3 Course: Begineer to Advanced
'''

import re
print('Magical Calculator')
print("Type 'quit' to exit application")

previous = 0
run = True

def performMath():
    global run
    global previous

    equation = ""
    if previous == 0:
       equation = input('Enter Equation: ')
    else:
        equation = input(str(previous))


    if equation == 'quit':
        print("Logging you out of our calculator!")
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()" "]','', equation) #use regex to filter user input & tell our program what kind of characters it should accept
        
        if previous == 0:
            previous = eval(equation) #built in function to handle complex mathematical operation from string
        else:
            previous = eval(str(previous) + equation)


while run:
    performMath()