### Exploring String types in Python;
space = " "
x = 10
string = "Hello World"
first = "Neeraj"
middle = "Singh"
last = "Junior"
name = first + space + middle + space + last
# print(name[0:9])
# print ("Instance: ", string[1:10])

## String Length in python;
# length = len(name)

## Different styles of print()
# Method 1: 
# Caution: Display is defined in brackets;
# print(name[0:1], '\n')
# print(name[1:2], '\n')
# print(name[2:3], '\n')

# Method 2:
# Warning: end="\n" not valid for python2;
# print(name[0:1], end="\n")
# print(name[1:2], end="\n")
# print(name[2:3], end="\n")

# Method 3:
# Caution: Display is defined in brackets;
# print(name[0:1],)
# print(name[1:2],)
# print(name[2:3],)

# print(length)
# for x in range(0, length):
#     print(name[x:], end="")

# for x in range(0, 10):
#     print('$'*x)

## String manipulations in python 3;
# print(name[:])
# print(name + " Singh")
# Checking concatenation;
# print(name + 23)

## 'N'=>0 'e'=>1 'e'=>2 'r'=>3 'a'=>4 'j'=>5

## Exploring String Slicing;
# print("Default: " + name[:])    # Neeraj
# print("Index 4: " + name[4:])   # aj
# print("Index 5: " + name[5:])   # j
# print("Index 3: " + name[3:])   # raj
# print("Index 0: " + name[0:])   # Neeraj
# print("Last Index 4:" + name[:4])   # Neer
# print("Index between 3 & 4: " + name[3:4])  # r
# print("Inde between 2 & 5:" + name[2:5])    # era


## Exploring string displaying stuffs;
# print("#"*4)    # Multiplication in String;
# print(first + " " + middle + " " + last)    # Concatenation String;
# print(name[0] + "|" + name[10] + "|" + name[18])   # Slice Operator;
# print(name[:], "|",name[10: 18])    # Slice Operator with Range;
# print('z' in name)  # Membership Operator;
# print('z' not in name) # Inverse Memebership Operator 
# print('C://Microsoft/MyFiles/')

## String join in python;
name = ["Neeraj", "Singh", "Junior"]
space = "|"
print(space.join(name))