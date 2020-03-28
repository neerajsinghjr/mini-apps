### Exploring built-in function in python 3;
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
sum_a = [12,213,455,5656,78787889,8989]
print(sum(sum_a))
