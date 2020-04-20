### Identity Operator: 'is' | 'is not' in python;

## Example 1: is operator in python 
# try:
#     num_a = int(input("Your number a: "))
#     num_b = int(input("Your number b: "))
    
#     if num_a is num_b:
#         print("Identity Matched !")
#     else:
#         print("Identity Not Matched !")
    
# except Exception as error:
#     print("Exception: ", error)
    
# finally: 
#     print("End !")
    
## Example 2: 'is' operator in python  
# try:
#     num_a = 12
#     num_b = '12'
    
#     if num_a is num_b:
#         print("Identity Matched !")
#     else:
#         print("Identity Not Matched !")
    
# except Exception as error:
#     print("Exception: ", error)
    
# finally: 
#     print("End !")

## Example 3: 'is not' operator in python
try:
    num_a = int(input("Your number a: "))
    num_b = int(input("Your number b: "))
    
    if num_a is not num_b:
        print("Identity is not Matched !")
    else:
        print("Identity Matched !")
    
except Exception as error:
    print("Exception: ", error)
    
finally: 
    print("End !")