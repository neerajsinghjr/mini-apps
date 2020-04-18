### Written on python 3 Interpreter;

############ 28 March 2020

## Program: Multiplication Table;
# try:
#     number = int(input("Your number: "))
#     for x in range(1, 11):
#         print("%d x %d = %d"%(number, x, number*x))

# except Exception as error:
#     print("Something went wrong. ", error)

## Program: Control Statement using List;
# try:
#     myList = [12, 15, 32, 42, 55, 75, 122, 132, 150, 100, 200]
#     for x in myList:
#         if x>120:
#             break
#         elif x%5 == 0:
#             print("Your number: ", x)
#         else:
#             continue

# except Exception as error:
#     print("Something went wrong.", error) 


############ 29 March 2020;

# Program: Convert Kilo To Miles;
# def changeKiloToMiles(number):
#     return number*0.621371
# try:
#     number = int(input("Enter KM: "))
#     print("Miles: ", changeKiloToMiles(number))
# except ValueError:
#     print("Something unexcepted occured ...")

## Program: Find the largest among three;
# try:
#     num = 0
#     myList = []
#     for x in range(0, 3):
#         temp = int(input("Enter number: "))
#         myList.append(temp)
#     print(max(myList))

# except ValueError:
#     print("Something went wrong ...")

## Program: Print 'Yes', if number is prime and even else 'no'
# def checkPrime(number):
#     if number > 1:
#         for x in range(2, number//2):
#             if number%x == 0:
#                 return False
#             else:
#                 return True
#     else:
#         return False

# def checkEven(number):
#     if number%2 == 0:
#         return True
#     else:
#         return False

# try :
#     number = int(input("Your number: ")) 
#     if checkPrime(number) and checkEven(number):
#         print("Yes it is even and also a prime")
#     else:
#         print("Sorry !")
#         print("Prime True") if checkPrime(number) else print("Prime False")
#         print("Even True") if checkEven(number) else print("Even False")
        
# except ValueError:
#     print("Something unexcepected occur ...")

# finally:
#     print("Thank you !")

## Program: Print the union and intersection of all even and odd [0, 20]
# try:
#     even = set()
#     odd = set()

#     for x in range(0, 21):
#         if x%2 == 0:
#             even.add(x)
            
#         else:
#             odd.add(x)

#     print("Union: ", even|odd)
#     print("Intersection: ", even&odd)

# except ValueError:
#     print("Something unexcepected occurred ...")

# finally:
#     print("Thank you !")


############ 30 March 2020;

## Program: Replace all 'a' with 'e' in string;
# str_a = "Train"
# str_b = "Program"

# print(str_a.replace('a', 'e'))
# print(str_b.replace('a', 'e'))

## Program: find length of sring "Refrigerator"
# try:
#     string = "Refrigerator"
#     print("Length of %s: %d" %(string, len(string)))

# except Exception as error:
#     print("Error: ", error)

# Program: Print each character of name in new line;
# try:
#     string = input("Your String: ")
#     for x in string:
#         print(x)

# except Exception as error:
#     print("Error: ", error)

## Program: Split string from '.' inside "Very.Easy.Assignments"
# try:
#     string = 'Very.Easy.Assignments'
#     print(string.split('.'))    
#     print(string.split('.', 0))
#     print(string.split('.', 1))

# except Exception as error:
#     print("Exception: ", error)


############ 31  March 2020;

## Program: List manipulation;
# even = []
# odd = []
# merge = []
# for x in range(0, 20):
#     if x%2 == 0:
#         even.append(x)
#     else:
#         odd.append(x)

# # CASE 1: Length of both list;
# print("Even: %d" %(len(even)))
# print("Odd: %d" %(len(odd)))

# # Case 2: Display Last 5 Element;

# print(even[-5:])
# print(odd[-5:])

# # Case 3: Delete 4th Element of list;
# del even[4]
# del odd[4]
# print(even, ' || ', odd)

# # Case 4: Replace 4 element by 'Junior Devil'
# even[4] = 'Junior Devil'
# odd[4] = 'Junior Devil'
# print(even, '||', odd)

# # Case 5: Merge both list;
# merge = even + odd
# merge.sort()
# print("Merge: ", merge)

## Program: Sum all the elements in the List;
# items = []
# for x in range(2, 200, 2):
#     items.append(x)
# print("Items Sum: ", sum(items))

## Program: find largest and smallest number from a list of lenght 5;
# try:
#     numbers = []
#     for x in range(0, 5):
#         temp = int(input("Your number %d: " %(x+1)))
#         numbers.append(temp)

#     print("List: ", numbers)
#     print("Max: ", max(numbers))
#     print("Min: ", min(numbers))

# except ValueError as val:
#     print("ValueError: ", val)

# except Exception as error:
#     print("Unhandled exception.", error)


############ 1 April 2020;

## Program: Generate 6 random numbers between 1 to 6;

# import random
# try:
#     randList = []
#     for x in range(0, 6):
#         temp = random.randint(1, 6)
#         randList.append(temp)
#         print("Iteration %d: %d" %(x+1, temp))
#     print("Random List: ", randList)

# except Exception as error: 
#     print("Unhandled exception occurred.", error)
    
    
## Program: Recursion(), Call this func inside itself and break completion of 10 cycle;

# try:
#     def recursion(number, count):    
#         if count == 10:
#             return number
#         else:
#             return (number+recursion(number+1, count+1))
                
#     number = int(input("Your number: "))
#     print(recursion(number, 0))
    
# except Exception as error:
#     print("Unhandled exception occurred.", error)


## Program: Enter 5 Employees - Names and Keys in Dictionary Structure;

# import os
# try:
#     emp = {}
#     empId = None
#     empName = None
#     print("Enter Details of New Employee ...")
#     for x in range(0, 2):
#         empId = input("Employee ID %d : " %(x+1))
#         empName = input("Employee Name %d: " %(x+1))
#         emp[empId] = empName        
#         os.system("cls||clear")
        
# ## Section: Access the empployee details using keys 

#     print("Search for Employees ...")
#     searchId = input("Employee ID: ")
#     if searchId in emp:
#         print("Employee's Name: %s" %(emp[searchId]))
#     else:
#         print("Sorry, Employee is not found !")
#         print("Exit ...")
        
# except Exception as error:
#     print("Exception occured. ", error)


############ 2 April 2020;

## Program: Generate a Dictionary to hold student roll with subjects, eg, roll: [subjects];
# import os
# try:
#     student = {}
#     subjects = []
#     roll = None   
#     temp = None
#     print("Welcome to Student Maintenance System ...")
#     for x in range(0, 2):
#         tempList = []
#         roll = input("Student %d Roll No: " %(x+1))
#         count = int(input("Total No Of Subjects: "))
#         for y in range(0, count):
#             temp = input("Subject %d: " %(y+1)) 
#             tempList.append(temp)
#         subjects.append(tempList)
#         student[roll] = subjects[x]
#         subjects.clear()
#         os.system("cls||clear")
#     #Display Data;
#     print(student)

# except Exception as error:
#     print("Unhandled Exception occured.", error)

## Program: Generate list of 20 Prime Numbers;
# def generatePrime():
#     prime = []
#     for x in range(2, 100):
#         count = 0
#         if len(prime) == 20:
#             return prime
#         else:
#             for y in range(1, x+1):
#                 # if count is not more than 3
#                 if x%y == 0:
#                     count = count + 1

#             # Check if count is less than 3
#             if count < 3 and count != 0:
#                 prime.append(x)

#     return prime

# prime = generatePrime()
# print("Prime List: ", prime)            
# print("Prime List Type: ", type(prime))            
    
## Program: Convert a list in into set;

# primeSet = set(generatePrime())
# print("Prime Set: ", primeSet)
# print("Prime Set Type", type(primeSet))

## Program: WAP to create a set of first 20 even numbers and perform intersection with the prime number set in question 3

# def generateEven():
#     even = set()
#     for x in range(1, 50):
#         if len(even) == 20:
#             return even
#         else:
#             if x%2 == 0:
#                 even.add(x)
#     return even

# evenSet = generateEven()
# primeSet = set(generatePrime())
# crossSet = evenSet&primeSet
# print(evenSet)
# print(primeSet)
# print(crossSet)

# ########## 3 April 2020;

# ## Program: Print every character in new line of loop;
# try:
#     count = 1
#     string = input("Your String: ")
#     for x in string:
#         print("Line %d: %s" %(count, x))
#         count = count + 1
    
# except Exception as error:
#     print("Exception occured.", error)

## Program: Check if 'orange' is in 'orange juice'
# try:
#     search = 'orange'
#     string = 'orange juice'
#     if search in string:
#         print("Search '%s' is Found in '%s'" %(search, string))
#     else:
#         print("Search '%s' not Found" %(search))
        
# except Exception as error:
#     print("Exception occured.", error)

## Program: Take full name and convert to this pattern, For e.g, R.B.Roser.
# try:
    # Method 1: 
    # fullName = input("Your full name: ")
    # formalName = ""
    # split = fullName.split(" ")
    # for x in len(split)-1:
    #     count = 1
    #     for y in x:
    #         if count == 1:
    #             formalName += y
    #         else:
    #             break
    # print(formalName)
            
    # Method 2: 
    # first = input("first: ")
    # mid = input("middle: ")
    # last = input("last: ")
    # name = first[0].upper()+"." + mid[0].upper() + "." + last.title()
    # print("Hi, %s" %(name))

# except Exception as error:
#     print("Unhandled Exception Occured.", error)

## Program: Generate a string and make a new one;
# try:
#     newString = ""
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     oldString = input("Your String: ")
#     for x in oldString:
#         if x in vowels or x == " ":
#             newString += x
#         else:
#             continue
#     print(newString)

# except Exception as error:
#     print("Unhandled Exception Occured.", error)


############ 06 April 2020;

## Program: Find out the largest word in the string "This is an umbrella";
# try:
#     # Helping Variables;
#     string = input("Your String: ")
#     splitArray = string.split(" ")
#     maxLen = []
#     maxValue = []

#     # Logic implementations;
#     for x in splitArray:
#         if len(maxLen) == 0 and len(maxValue) == 0:
#             maxValue.append(x)
#             maxLen.append(len(x))
#         else:
#             if maxLen[0] < len(x):
#                 maxLen.clear()
#                 maxValue.clear()
#                 maxLen.append(len(x))
#                 maxValue.append(x)

#             elif maxLen[0] == len(x):
#                 maxLen.append(len(x))
#                 maxValue.append(x)

#             else:
#                 continue
    
#     # Iterating over two list together;
#     for x, y in zip(maxValue, maxLen):
#         print("Max Value: %s with Length: %d" %(x, y))

# except Exception as error:
#     print("Unhandled Exception.", error)


## Program: Python program to count the number of characters (character frequency) in a string 
## Sample String : 'google.com'
##  Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
# try:
#     strDic = {}
#     string = input("Your String: ")
#     for x in string:
#         len = string.count(x)
#         strDic[x] = len
        
#     # Displaying data;
#     print(strDic)

# except Exception as error:
#     print("Unhandled Exception.", error)


## Program: Write a Python to print this pattern:
# 55555
# 4444
# 333
# 22
# 1

# try:
#     for x in range(5, 0, -1):
#         for y in range(0, 5):
#             if (y < x):
#                 print(x, end=" ")
#         print()

# except Exception as error:
#     print("Unhandled Exception: ", error)


############ 07 April 2020;

## Program: Calculate length of a String without using len() function
# try:
#     len = 0
#     string = input("Your String: ")
#     for x in string:
#         len += 1
#     print("Length of %s is %d" %(string, len))

# except Exception as error:
#     print("Unhandled Exception.", error)


## Program: Check if a given number is in range , Take Number, And range as input from user
# try:
#     number = int(input("Your Number: "))
#     lower = int(input("Lower Range: "))
#     upper = int(input("Upper Range: "))
#     print("Found, Successfull !") if number in range(lower, upper) else print("Not Found !")

# except Exception as error:
#     print("Unhandled Exception.", error)


## Program: Program to Find Factorial of Number Using Recursion
# try:
#     def fact(number):
#         if number == 1:
#             return number
#         else:
#             return (number * fact(number-1))
        
#     number = int(input("Your Number: "))
#     print(fact(number))

# except Exception as error:
#     print("Exception Occured. ", error)


############ 08 April 2020;

## Program: String inbuilt 5 functions;
# try:
#     string = input("Your String: ")
#     print("1. Convert To Lowercase: %s" %(string.lower()))
#     print("2. Convert To Uppercase: %s" %(string.upper()))
#     print("3. String Split Func: %s" %(string.split(" ")))
#     print("4. Check if Lowercase: %s" %(string.islower()))
#     print("5. Check if uppercase: %s" %(string.isupper()))
    
# except Exception as error:
#     print("Exception Occured.", error)


############ 09 April 2020;

## Program: To Perform Addition, Subtraction, Multiply, Divide, Exit;
# import os;
# try:
#     # Printing menu board;
#     def printMenu():
#         print(" __________________________ ")
#         print("|                          |")
#         print("|______ 1. Addition _______|")
#         print("|______ 2. Subtraction ____|")
#         print("|______ 3. Multiplication__|")
#         print("|______ 4. Divide _________|")
#         print("|______ 5. Exit ___________|")
#         print("|__________________________|")
#         choice = int(input("Your Choice: "))
#         return choice

#     # Calculating output;
#     def calculate(first, second, choice):
#         if choice == 1:
#             return first+second
#         elif choice == 2:
#             return first-second
#         elif choice == 3:
#             return first*second
#         else:
#             if second != 0:
#                 return first/second
#             else:
#                 return False
        
#     # main program calls;
#     choice = printMenu()
#     while choice < 6:
#         if choice > 0 and choice < 5:
#             first = int(input("Your First Number: "))
#             second = int(input("Your Second Number: "))
#             result = calculate(first, second, choice)
#             if result is not False:
#                 print("Result: %f" %(result))
#                 choice = input("Continue or Exit (y/n)")
#                 if choice == 'y' or choice == 'Y' or choice == 'Yes' or choice == "YES":
#                     os.system("cls||clear")
#                     choice = printMenu()
#                 else:
#                     print("Thank You, Successfully Ends ....")
#                     break
#             else:
#                 print("Result is reach Unsuccessfull")
#                 print("Check your entered input")

#         else:
#             print("Thank You !") 
#             break
            
# except Exception as error:
#     print("Exception Occured. ", error)


# ## Program: sum all the numbers in a list of 10 elements input by the user;
# try:
#     sum = 0
#     temp = 0
#     list = []
#     for x in range(0, 10):
#         temp = int(input("Your Number %d: " %(x+1)))
#         list.append(temp)
#         sum += temp
#     print("Your List: ", list)
#     print("Sum: ", sum)

# except Exception as error:
#     print("Exception Occured. ", error)


## Program: List of rainbow colours, remove 1, 3, last;
# try:
#     temp = 0
#     name = "RAINBOW"
#     rainbow = {}
#     print("RAINBOW Colours List ...")
#     for x in name:
#         temp = input("%s means: " %(x))
#         rainbow[x]=temp
#         # rainbow.append(temp)
    
#     # Display full;
#     print(rainbow)
#     # Deleting Elements;
#     rainbow.pop('R')
#     rainbow.pop('A')
#     rainbow.pop('W')
#     print(rainbow)
    
        
# except Exception as error:
#     print("Exception Occured. ", error)
    

## Program: Merge two list using + operator;
# try:
#     even = []
#     odd =[]
#     list = []
#     for x in range(0, 20):
#         if x%2 == 0:
#             even.append(x)
#         else:
#             odd.append(x)

#     list = even+odd

#     print("Even: " ,even)
#     print("Odd: ", odd)
#     print("List: ", list)

# except Exception as error:
#     print("Exception Occured. ", error)


############ 13 April 2020;

# Program: Insert given string X into 2nd position in list Y
# list = [10 ,20 ,30 ,50]
# print("Before Insertion: ", list)
# list.insert(2, 10000)
# print("After Insertion: ", list)

# Program:
# Q1: Create empty dictionary and then add multiple elements .
# Q2: Program: add key to a dictionary and print all the values

# try:
#     temp="";
#     student={}
#     count=int(input("Enter number of student: "))
#     for x in range(0, count):
#         temp=input("Student Name [%d]: " %(x+1))
#         student[x]=temp
#     print("Keys: ", student.keys())
#     print("Values: ", student.values())
#     print("Dictionary: ", student)

# except Exception as error:
#     print("Exception catch.", error);


# Program: Add dict2 elements into dict1 and print it , use update 
# dict1 = {1: "one", 2: "three"}
# dict2 = {2: "two"}

# dict1.update(dict2)
# print(dict1)


############ 15 April 2020;

## Program: Change the first and last character of the string;
# try: 
#     newString = ""
#     string = input("Enter String: ")
#     first = input("Enter first Character: ")
#     last = input("Enter last Character: ")
#     for x in range(0, len(string)):
#         if x == 0:
#             newString += first
#         elif x == len(string)-1:
#             newString += last
#         else:
#             newString += string[x]
    
#     print("Your String: %s" %(newString))

# except Exception as error: 
#     print("Exception catch !", error)

## Program: Input from the user and displays that input back in upper and lower cases;
# try: 
#     string = input("Enter String: ")
#     print("Uppercase: %s" %(string.upper()))
#     print("Lowercase: %s" %(string.lower()))

# except Exception as error: 
#     print("Exception catch !", error)

## Program: Remove the characters which have odd index values of a given string.
# try:
#     strOdd= ""
#     string = input("Your String: ")
#     for x in range(0, len(string)):
#         if x%2 != 0:
#             strOdd += string[x]
    
#     print("String Without Odd Index: %s" %(strOdd))

# except Exception as error: 
#     print("Exception catch !", error);


############ 16 April 2020;

## Program: to get the largest number from a list.
# try: 
#     temp = 0
#     myList = []
#     items = int(input("How many items are there: "))
#     for x in range(0, items):
#         temp = input("List [%d]: " %(x+1))
#         myList.append(temp)
#     print("Max Element: %s" %(max(myList)))

# except Exception as error:
#     print("Exception catched !")
#     print("Error: ", error)

# finally:
#     print("Thank You!")


## Program: to multiplies all the items in a list.
# try: 
#     list = [12, 13, 15, 16, 20]
#     newList = list * 2
#     print("Original List: ", list)
#     print("Mulitiplied List: ", newList)
    
# except Exception as error:
#     print("Exception catched !")
#     print("Error: ", error)

# finally:
#     print("Thank You!")


## Program: to remove duplicates from a list.
# try: 
#     duplicatedList = [12, 13, 15, 16, 20, 12, 13, 15, 16, 20]
#     print("Original Duplicated List ... \n", duplicatedList)
#     # Remove duplicacy;
#     filteredSet = set(duplicatedList)
#     # Converting to list;
#     filteredList = list(filteredSet)
#     print("Filter List ... \n ", filteredList)

# except Exception as error:
#     print("Exception catched !")
#     print("Error: ", error)

# finally:
#     print("Thank You!")


############ 17 April 2020;

## Program: Function that takes two lists and returns True if they have at least one common member.
# try: 
#     # Check intersection between two list;
#     def checkIntersection(firstList, secondList):
#         firstSet = set(firstList)
#         secondSet = set(secondList)
#         value = firstSet.intersection(secondSet)
#         if value:
#             return True
#         else :   
#             return False

#     # building program ladders;
#     def makeProgram():
#         temp = 0
#         firstList = []
#         secondList = []
#         firstCount = int(input("Enter number of element in List A: "))
#         secondCount = int(input("Enter number of element in List B: "))
#         # Taking values of List A;
#         for x in range(0, firstCount):
#             temp = input("List A [%d]: " %(x+1))
#             firstList.append(temp)
        
#         # Taking values in List B;
#         for x in range(0, secondCount):
#             temp = input("List B [%d]: " %(x+1))
#             secondList.append(temp)

#         # Checking Intersection;
#         if checkIntersection(firstList, secondList) == True:
#             print("True")
#         else:
#             print("False")

#     # main program execution;
#     makeProgram()
        
# except Exception as error:
#     print("Exception catched !")
#     print("Error: ", error)

# finally:
#     print("Thank You!")

## Program: to convert a list of characters into a string.
# try: 
#     charList = ['a' , 'e', 'i', 'o', 'u']
#     print("Character List \n", charList)
#     print("Type of Character List \n", type(charList))
#     strList = str(charList)
#     print("String Character List \n", strList)
#     print("Type of String Character List \n", type(strList))

# except Exception as error:
#     print("Exception catched !")
#     print("Error: ", error)

# finally:
#     print("Thank You!")

# # Program: to find common items from two lists.
# try: 
#     # Check intersection between two list;
#     def checkIntersection(firstList, secondList):
#         firstSet = set(firstList)
#         secondSet = set(secondList)
#         values = firstSet.intersection(secondSet)
#         if values:
#             print("Intersecting Values ... \n", values)
#         else :   
#             print("Sorry, No Intersecting Values Found !")

#     # building program ladders;
#     def makeProgram():
#         temp = 0
#         firstList = []
#         secondList = []
#         firstCount = int(input("Enter number of element in List A: "))
#         secondCount = int(input("Enter number of element in List B: "))
#         # Taking values of List A;
#         for x in range(0, firstCount):
#             temp = input("List A [%d]: " %(x+1))
#             firstList.append(temp)
        
#         # Taking values in List B;
#         for x in range(0, secondCount):
#             temp = input("List B [%d]: " %(x+1))
#             secondList.append(temp)

#         # Checking Intersection;
#         checkIntersection(firstList, secondList)

#     # main program execution;
#     makeProgram()

# except Exception as error: 
#     print("Exception Catched !")
#     print("Exception: ", error)

# finally:
#     print("Thank You!")