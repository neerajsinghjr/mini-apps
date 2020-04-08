### Exploring Modules in python;

import Modules.general.pyMathsTable as table

try:
    # print(" ______________________________________")
    # print("|__________Menu on the Table___________|")
    # print("|__________1. Calculate Table _________|")
    # print("|__________2. Check Even ______________|")
    # print("|__________3. Check Prime______________|")
    # print("|__________4. Check Odd _______________|")
    # print("|__________5. Exit_____________________|")

    # dir(): return the list of names defined in passwd modules;
    print(dir(table))
    
    # reload(): used to reload the modules;
    # reload(table)
    
    # choice = int(input("Your number: "))
    # options = {
    # }

    # number = int(input("Your number: "))
    # table.table(number)

except Exception as error:
    print("Error", error)