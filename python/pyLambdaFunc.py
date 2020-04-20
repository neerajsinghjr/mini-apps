### Exploring the use of lambda function;

## Example 1;
# square = lambda x: x**2
# number = int(input("You number: "))
# print(square(number))

## Example 2;
# try :
#     def table(number):
#         return lambda iteration: number*iteration
    
#     number = int(input("Your number: "))
#     result = table(number)
#     for x in range(1, 11):
#         print("%d x %d = %d" %(number, x, result(x)))

# except ValueError:
#     print("Something unexpected occurred ...")

# finally: 
#     print("End !")
    
## Example 3;
# try :
#     prime = []
#     even = []
#     odd = []
    
#     for x in range(1, 101):
#         # even & odd checkpoint;
#         if filter(lambda x: x%2 == 0, even):
#             even.append(x)
#         else:
#             odd.append(x)
#         # prime number checkpoint;
#         if x > 1:
#             for y in range(2, x//2):
#                 if x%y != 0:
#                     prime.append(x)
                    
#     # printing;
#     print(even)
    
# except ValueError:
#     print("Something unexpected occured ...")

## Example 4: 
List = [3545,56,56,56,7,6,87,87,855,53,535,34535224234,234,23,232,3,23,2,42,235,34534,53,453,5,35,56]
oddList = filter(lambda x: (x%2 != 0), List)      # filter return bundle, use by list() func
print(list(oddList))

