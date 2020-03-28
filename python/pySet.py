### Python Set For Storing Miscellaneous data;
## Simplex set in python;
# days_a = {"mon", "tue", "wed", "thur", "fri", "sat", "sun"}
# print(type(days_a))

## Testing list complex;
# days_b = set([{"mon", "tue", "wed", "thur", "fri", "sat", "sun"}, {"mon", "tue", "wed", "thur", "fri", "sat", "sun"}])

# print(type(days_b), days_b)

# for x in days_b:
    # print(x, "|", type(days_b))
    
## Testing another complex;
# days_b = {
#     'key_a' : "monday",
#     'key_b' : "tueday",ss
#     'key_c' : "wednesday",
#     'key_d' : "thursday",
#     'key_e' : "friday",
#     'key_f' : "saturday",
#     'key_g' : "sunday",
# }

# for x in days_b:
    # # print(x, ":", days_b[x])
    # # print(x,":",days_b.get(x, 'not found'))
    # data = days_b.get(x)
    # if data:
    #     print(data, "is Found @ ", x)
    # else:
    #     print("Not Found!")

# Testing case 2;
# days_c = {
#     "monday", 1, "tuesday", 2, 'wednesday', 3, 2*4
# }

# print(type(days_c))
# print(days_c)

## Testing the set() method;
# Days = set(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])  # list inside set() - pass
# Days = set(("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"))  # tuple inside set() - pass
# Days = set({ '1': "Monday", '2': "Tuesday", '3': 'Wedneday', '4': 'Thursday'})  # dictionary inside set()
# print(Days)  
# print(type(Days))  

## Set checking duplicacy;
# number = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# print(type(number))
# print(number)

# number = set(number)
# print(type(number))
# print(number)

# number.clear()
# number.remove('Tuesday')

# print("Number", '|', number)

## Intersection: It work on new sets;
a = {"ayush", "bob", "dude"}  
b = {"castle", "dude", "emyway"}  

print(a)
print(a.intersection(b))

## Intersection_update(): It work on original sets;
a = {"ayush", "bob", "castle"}  
b = {"castle", "dude", "emyway"}  
c = {"fuson", "dude", "castle"}  
  
# a.intersection_update(b, c)    

## Frozen set in Set;
# a = frozenset({'1', '2'})
# print(a)
# a.add('22')