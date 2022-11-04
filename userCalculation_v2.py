## Our user driven calculator program, version 2

# a function that prints the help menu for the user
def printHelpMenu():
    print("To do addition, input: a or A")
    print("To do subtraction, input: s or S")
    print("To do multiplication, input: m or M")
    print("To do division, input: d or D")
    print("To exit the program, input: e or E")

# a function that takes in input from the user
def getUserInput(kind):    
    # a boolean value for toggling control of our while 
    flag = True
    
    # for when we are expecting a string to be input
    if kind == 'l':
        while flag == True:
            # take in user input
            selection = input()
            # enter loop if user input is a valid menu option
            if selection in ['a','A','m','M','s','S','d','D','e','E']:
                flag = False
            else:
                print("please enter only valid menu options")
    
    # for when we are expecting an integer to be input
    elif kind == 'n':
        try:
            selection = int(input())
        except:
            print("please enter valid integers only")
    return selection

##
# Program begins below
##

print("Welcome. Please select a calculation to perform by inputting the appropriate number.")

printHelpMenu()

menuSelection = getUserInput('l')
print("You selected: ", menuSelection)

while menuSelection != 'e' and menuSelection != 'E':

    if menuSelection == 'a' or menuSelection == 'A':
        print("please enter your first number")
        x = getUserInput('n')
        print("Please enter a second number to add to the first")
        y = getUserInput('n')
        answer = x + y
        print("Your answer is ", x, "+", y, "=", answer)

    elif menuSelection == 's' or menuSelection == 'S':
        print("please enter your first number")
        x = getUserInput('n')
        print("Please enter a second number to subtract from the first")
        y = getUserInput('n')
        answer = x - y
        print("Your answer is ", x, "-", y, "=", answer)

    elif menuSelection == 'd' or menuSelection == 'D':
        print("please enter your first number")
        x = getUserInput('n')
        print("Please enter a second number to divide into the first")
        y = getUserInput('n')
        answer = x / y
        print("Your answer is ", x, "/", y, "=", answer)

    elif menuSelection == 'm' or menuSelection == 'M':
        print("please enter your first number")
        x = getUserInput('n')
        print("Please enter a second number to multiply to the first")
        y = getUserInput('n')
        answer = x * y
        print("Your answer is ", x, "*", y, "=", answer)
        
    menuSelection = getUserInput('l')
    
print('the program is now terminating...')
