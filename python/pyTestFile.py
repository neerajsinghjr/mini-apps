# try:
#     string = input("Your String: ")
#     print("1. Convert To Lowercase: %s" %(string.lower()))
#     print("2. Convert To Uppercase: %s" %(string.upper()))
#     print("3. String Split Func: %s" %(string.split(" ")))
#     print("4. Check if Lowercase: %s" %(string.islower()))
#     print("5. Check if uppercase: %s" %(string.isupper()))
    
# except Exception as error:
#     print("Exception Occured.", error)

import os

# Check For Positive;
def checkIfPositive(number):
    if number > 0:
        # print("Positive Number: %d" %(number))
        return True
    return False

# Check For Negative;
def checkIfNegative(number):
    if number < 0:
        return True
    return False
        
# Check For Even;
def checkIfEven(number):
    if number == 0:
        return False
    elif number %2 == 0:
        return True
    return False
    
def checkIfOdd(number):
    if number %2 != 0:
        return True
    # return to main;
    return False

def checkIfZero(number):
    if number == 0:        
        return True
    # returnt to main;
    return False
    
    
try:
    number = 0
    myList = []
    # Creating list;
    for x in range(0, 5):
        number = int(input("Enter Value at Index %d: " %(x+1)))
        myList.append(number)
    # Checking List;
    for number in myList:
        # Check For Positive;
        if checkIfPositive(number):
            print("Positive: ", number)
            # Check For Even and Odd;
            if checkIfEven(number):
                print("Even Number: ", number)
            else:
                print("Odd Number: ", number)
        # Check for Negative;
        elif checkIfNegative(number):
            print("Negative: ", number)
        # Check For Zeros;
        elif checkIfZero(number):
            print("Zero: ", number)
        else:
            print("Something unexpected occured !");

    # os.system("cls || clear")
    # Searching in list;
    
except Exception as error:
    print("Exception traced.", error)

else:
    print("Program Terminates Successfully ...")

finally:
    print("Exiting ...")
