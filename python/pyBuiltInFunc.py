### Exploring built-in function in python 3;

## Summary:

# print()|input()|range()|int()|str()|list()|tuple()|dict()|set()|all()|any()|abs()|hex()|slice()|sorted()
# getattr()|setattr()|delattr()| hasattr()||type()|isinstance()|bin()|bool()|compile()|exec()|iter()|next()
# callable()|sum()|eval()|float()|help()|len()|oct()|open()|ord()|reversed|pow()|round()|complex()|
# max()|min|append()|remove()|add()|object()|id()|hash()
# locals()|vars()|zip()

## End:

## abs(): returns absolute positive value or magnitude;
# num1 = -20
# num2 = -20.0987
# num3 = 20
# num4 = 20.23456789
# num5 = 0.23456789
# print(abs(num1), abs(num2), abs(num3), abs(num4), abs(num5))

## all(): check for iterable objects;
# list_a = [0, False, 12, 14, 15]       # False
# print("Case 1: ", all(list_a))
# list_b = [0, 12, 14, 15]              # False
# print("Case 2: ", all(list_b))
# list_c = [3, 4, 6]                    # True
# print("Case 3: ", all(list_c))
# list_d = []                           # False
# print("Case 4: ", all(list_d))

## bin(): return binary
# number = 20
# print(bin(number))
# number = "Neeraj"
# print(bin(number))

## bool(): return if data is there;
# temp_a = 234567890
# temp_b = []
# temp_c = ['10']
# temp_d = {}
# temp_e = {"name":"Neeaj Singh"}
# print(bool(temp_a))
# print(bool(temp_b))
# print(bool(temp_c))
# print(bool(temp_d))
# print(bool(temp_e))

## bytes(): return everything of 
# num = 10
# string = "Neeraj"
# print(bytes(num))
# print(bytes(string, 'utf-8'))

## callable(): check it is callable or not 
# def square(x):
#     return x**2
# # x = int(input("Your number: "))
# if isinstance(x, int) != False:
#     print("Callable: ", callable(square))
#     print("Callable: ", callable(x))
#     print("Square: ", square(x))    
# else:
#     print("Something unexcepted occurred...")

## isinstance(): Exploring stuffs;
# num = 34567890
# string = "sdfghjkl"
# print(isinstance(num, int))
# print(isinstance(string, int))

# x = input("Enter anything: ")
# print(int(x))
# print(type(x))

## compile(): compiles the code which can execute later;
## ASK: Not running good;
# num = 'x=input("Your Number: ") \nprint("Cube: ", x**3)'
# compiledCode = compile(num, 'pyBuiltInFunc.py', 'exec')
# exec(compiledCode)

## exec(): allows dynamic execution of code inside quote;
# x = 10
# string = "print(x**2)"
# exec(string)

## any(): iterates over single value unlike all()
# list_a = [0, False, 12, 14, 15]     # True
# print("Case 1: ", any(list_a))
# list_b = [0, 12, 14, 15]            # True
# print("Case 2: ", any(list_b))  
# list_c = [3, 4, 6]                  # True
# print("Case 3: ", any(list_c))
# list_d = []                         # False
# print("Case 4: ",any(list_d))

## ascii(): print the ascii character encoding; 
# normalText = "Python is a programming language !!!"
# print(ascii(normalText))

## eval(): evaluates a given string;
# x = 64
# y = "x**2 + x**3"
# print(y, eval(y))

## globals(): ?

## iter(): return iterator object and return one element at a time;
# temp = [0, False, 12, 14, 15] 
# counter = iter(temp)
# print(next(counter))

## locals(): returns the dictionary of the current local symbol table
# def localsAbsent():  
#     return locals()  
  
# def localsPresent():  
#     present = True  
#     list_a = [123,234,5654,234,65432]
#     print("-->", list_a)
#     return locals()  
  
# print('localsNotPresent:', localsAbsent())  
# print('localsPresent:', localsPresent())

## open() : function used to open file;
# file = open('/var/www/html/modules/python/pyFileObject.py')

## sum(): return the sum;
# sum_a = [12,213,455,5656,78787889,8989]
# print(sum(sum_a))

## map(): return an list after applying a given function to each iteration;
# def square(x):
#     return x+x

# x = [1, 2, 3, 4, 5]
# result = map(square, x)
# print(result)

# resultSet = dict(result)
# print(resultSet)

## object(): returns an empty object, holds the built-in properties;
# python = object()
# print(python)
# print(dir(python))

## complex(): converting a number to complex number;
# number = 5678
# print(complex(number, 9876))

## getattr() | setattr() | delattr(): one get, set and other one delete the attribute;
# class Student:
#     # Attributes 
#     studId = 100101
#     name = "Neeraj Singh"
#     roll = "1604051031"
#     email = "NeerajSingh@gmail.com"
    
#     # Init Constructor 
#     def __init__(self, name, roll, email):
#         self.id = id
#         self.name = name
#         self.roll = roll
#         self.email = email
        
#     # get method    
#     def getAttr(self):
#         print(self.id,"|", self.name, "|", self.roll, "|", self.email)

# neeraj = Student("neeraj", 23456789, 'devil@gmail.com')
# neeraj.getAttr()

## hash(): generate hash of the number
# print(hash(2))
# print(hash(3))
# print(hash(9))
# print(hash(22.345678))
# print(hash("Neeraj Singh Junior"))

## help(): return the help description of object passed as argument;
# print(help(self)) # Error: Self is not defined 
# print(help(print))
# print(help(help))

## hex(): convert decimal to hex
# print(hex(3456))

## id(): return the id of the selected 
# number = 435678
# string = "fdghjkl"
# mylist = [2345,654321,234567,765432,345678,8765432]

# print(id(number), "|", id(string), "|", id(mylist))

## sorted(): sort the elements;
# number = 435678
# string = "fdghjkl"
# mylist = [2345,654321,234567,765432,345678,8765432]
# mydic = {"first":"neeraj", 'middle': "singh", "last": "junior"}

# print(sorted(number))
# print(sorted(string), sorted(mylist), sorted(mydic))

## next(): used to fetch items from the collection.
# mylist = [2345,654321,234567,765432,345678,8765432]
# mydic = {"first":"neeraj", 'middle': "singh", "last": "junior"}

# item_l = iter(mylist)
# item_d = iter(mydic)
# print("Length: ", len(mydic))

# for x in range(0, len(mylist)):
#     print(next(item_l))

# for x in range(0, len(mydic)):
#     print(next(item_d))
    
## slice(): used to slice the elements from collections;
# string = "neeraj singh junior"
# myList = [234,432,2345,654323456,54323456543,21]

# index = slice(2, len(string), 4)
# index = slice(2, 5, 2)

# print(string[index])     # Output: e| |g|u|r
# print(myList[index])
 
## ord(): used to return unicode point for given character;
# print(ord('z'))

## pow(): used to power the number;
# print(pow(87, 3))

## reversed(): used to reverse list, tuple, dictionary;


## round(): used to round off the digit;
# print(round(98765.3))   ##  *65
# print(round(98765.4))   ##  *65
# print(round(98765.5))   ##  *66
# print(round(98765.6))   ##  *66
# print(round(98765.9))   ##  *66

# vars(): used to given the __dict__ type of current object;
# class Student:
#     # Attributes 
#     studId = 100101
#     name = "Neeraj Singh"
#     roll = "1604051031"
#     email = "NeerajSingh@gmail.com"
    
#     # Init Constructor 
#     def __init__(self, name, roll, email):
#         self.id = id
#         self.name = name
#         self.roll = roll
#         self.email = email
        
#     # get method    
#     def getAttr(self):
#         print(self.id,"|", self.name, "|", self.roll, "|", self.email)

# neeraj = Student("neeraj", 23456789, 'devil@gmail.com')
# print(vars(neeraj))

## zip(): used to return the zip object 
# numList = [56789,343212,4567,6521,24356]

# result = zip(numList)
# resultSet = set(result)

# print(result)
# print(resultSet)