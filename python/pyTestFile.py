try:
    string = input("Your String: ")
    print("1. Convert To Lowercase: %s" %(string.lower()))
    print("2. Convert To Uppercase: %s" %(string.upper()))
    print("3. String Split Func: %s" %(string.split(" ")))
    print("4. Check if Lowercase: %s" %(string.islower()))
    print("5. Check if uppercase: %s" %(string.isupper()))
    
except Exception as error:
    print("Exception Occured.", error)