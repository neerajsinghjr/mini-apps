### Table: Multiplication Table, require integer as argument;

## table(number): require number of type int;
try:
    def table(number):
        if isinstance(number, int) == True or int(number) == True:
            for x in range(1, 11, 1):
                print("%d x %d = %d" %(number, x, number*x))
        else:
            print("Something went wrong ...")

    def checkPrime(number):
        if isinstance(number, int) == True | int(number) == True:
            if number < 1:
                raise ValueError
            else:
                count = 0
                for x in range(2, number+1):
                    if number%x == 0:
                        count += 1
                if count == 1:
                    print("%d is Prime" %(number))
                else:
                    print("%d is not Prime" %(number))
        else: 
            print("Something went wrong ...")

except ValueError:
    print("Your number is too small")

except Exception as error:
    print("Error: ", error)