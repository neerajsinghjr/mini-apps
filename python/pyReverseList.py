list= [1, 2, 3, 4, 5, 6]

# Method 1: reversed() built in method;
reversed(list)  # not working;
print(list)

# Method 2: reverse() object in method;
# list.reverse();
# print(list)

# Method 3: slice operator in method;
print(list[::-1])   # Slice Operator in python

# List change value;
list[1:3] = [80, 90]
list.append(100)
list.insert(0, 0)
print(list)
print(len(list))
print(list*1000)