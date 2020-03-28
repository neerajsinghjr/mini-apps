### Written on python 3 Interpreter;

# Program: Convert Kilo To Miles;
def changeKiloToMiles(number):
    return number*0.621371
try:
    number = int(input("Enter KM: "))
    print("Miles: ", changeKiloToMiles(number))
except ValueError:
    print("Something unexcepted occured ...")

## Program: Find the largest among three;
try:
    num = 0
    myList = []
    for x in range(0, 3):
        temp = int(input("Enter number: "))
        myList.append(temp)
    print(max(myList))

except ValueError:
    print("Something went wrong ...")

## Program: Print 'Yes', if number is prime and even else 'no'
def checkPrime(number):
    if number > 1:
        for x in range(2, number//2):
            if number%x == 0:
                return False
            else:
                return True
    else:
        return False

def checkEven(number):
    if number%2 == 0:
        return True
    else:
        return False

try :
    number = int(input("Your number: ")) 
    if checkPrime(number) and checkEven(number):
        print("Yes it is even and also a prime")
    else:
        print("Sorry !")
        print("Prime True") if checkPrime(number) else print("Prime False")
        print("Even True") if checkEven(number) else print("Even False")
        
except ValueError:
    print("Something unexcepected occur ...")

finally:
    print("Thank you !")

## Program: Print the union and intersection of all even and odd [0, 20]
try:
    even = set()
    odd = set()

    for x in range(0, 21):
        if x%2 == 0:
            even.add(x)
            
        else:
            odd.add(x)

    print("Union: ", even|odd)
    print("Intersection: ", even&odd)

except ValueError:
    print("Something unexcepected occurred ...")

finally:
    print("Thank you !")