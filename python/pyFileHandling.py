### File Handlings in Input/Output;

import os;  # import to manipulate files and directory;


## Example 1: Checking opening of files;
# fileptr = open('DummyFiles/Student.txt', 'a+')

# if fileptr:
#     print("File opened successfully: ", fileptr)
# else:
#     print("Files Error", fileptr)
    
# fileptr.close()

# print("After Closing File: ", fileptr)

## Example 2: Reading from the file;
# try:
#     # Exploring different reading lines;
#     fileptr = open("DummyFiles/Student.txt", 'r')
#     for char in fileptr:
#         print(char, end=" ")
        
#     readline = fileptr.readline()
#     readlines = fileptr.readlines()    
#     print(type(readline), readline)       # return single line of type string;
#     print(type(readlines), readlines)     # return all lines of type list;
#     fileptr.close()
    
#     # Writing to file;
#     fileobj = open('DummyQuotes/Dream.txt', 'w+')
#     dream = "1. If you can dream it you can build it. If you can build it, you can live it."
#     fileobj.write(dream)
#     fileobj.close()
    
#     # Reading from file;
#     fileobj = open('DummyQuotes/Dream.txt', 'rb')
#     for char in readfile:
#         print(char)    
    
# except ValueError as val:
#     print("Value Error: ", val)

# except IOError as io:
#     print("IOError: ", io)
    
# except NameError as nam:
#     print("NameError: ", nam)
    
# except Exception as exe:
#     print("Something unexeprected occured ...",exe)

# else:
#     print("Work done successfully ...")

## Example 3: Reading and Writing to files;
# try:
#     string = "Be Brave, take risk, nothing can substitue experience !"
    # Open file using the read mode (r, r+, rb, rb+)
    # with open("DummyQuotes/lorem.txt", 'r+') as fileobj:
    #     print(fileobj.tell())
    #     fileobj.write("Hello World")
    
    # Open file using the write mode (w, w+, wb, wb+)
    # with open("DummyQuotes/moquote.txt", 'w+') as fileobj:
    #     print("Start: ", fileobj.tell())
    #     fileobj.write(string)
    #     print("End: ", fileobj.tell())
        
    # checkpoint if with closes the file;
    # fileptr = int(fileobj.tell())
    # print("temp: ", fileptr)
    
    # Reading file from file;
    # with open("DummyQuotes/moquote.txt", 'r') as fileobj:
        # Read all lines;
        # for lines in fileobj:
        #     print(lines)
        
        # read from specific lines;
        # fileptr = int(fileobj.tell())
        # print(fileobj.read(10))
        
    # Changing the pointer;
#     with open("DummyQuotes/moquote.txt", 'r') as fileobj:
#         fileobj.seek(15)
#         for data in fileobj:
#             print(data)
        

# except Exception as error:
#     print("Error: ", error)
    
## Manipulating files and creating directory;
# Renaming files;
# os.rename('DummyQuotes/moquote.txt', 'DummyQuotes/motivational.txt')
# os.rename('DummyQuotes/motivational.txt', 'DummyQuotes/Motivational.txt')

# mkdir() and rmdir()
# os.mkdir('DummyQuotes/myQuotes')
# os.mkdir('DummyQuotes/myQuotes/tmp')
os.rmdir('DummyQuotes/myQuotes/tmp')