### Checking greater number between the 3 random numbers;

try:
    a = int(input("You number: "))
    b = int(input("You number: "))
    c = int(input("You number: "))
    
    if a>b and a>c:
        print("You number %d is greater than %d, %d" %(a, b, c))
    elif b>a and b>c:
        print("You number %d is greater than %d, %d" %(b, a, c))
    else:
        print("You number %d is greater than %d, %d" %(c, a, b))
        
except Exception as error:
    print("Exception: ", error)

finally:
    print("End !")