### Checking if the number is even or odd;
number = int(input("Enter any number: "))
if type(number) != int:
    print("Error occured number is NAN")
else:    
    if(number%2 != 0):
        print(number, "is Odd")
    else:
        print(number, "is Even")