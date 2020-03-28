### Go through in loops - for, while, do while;

## Special Case: None data type;
# i = None
# print(type(i))

## For Loop: for-else statements
# for x in range(0, 10):
#     print(x)
# else:
#     print("End of For Loop")
    
## For Loop: Using break statement;
# Else won't run when the loop terminates conditionally;
# for x in range(0, 10):
#     if (x ==5):
#         break
#     print(x)
# else:
#     print("End of For Loop")

## For Loop: Iterating a String;
# name = "Neeraj Singh Junior"
# for x in name:
#     print(x,)

## For Loop: Iterating a list;    
# list = ['Neeraj', 'Singh', 'Junior']
# for x in list:
#     print(x)
    
## For Loop: Iterating a Dictionary;
# userList = [
#     {
#         'id' : 1,
#         'userId' : 'NeerajSingh511997',
#         'name' : 'Neeraj Singh Junior',
#         'email' : 'NeerajSingh511997@gmail.com',
#         'password' : '3456789kjhg@#$KJHG34567KJHGFDS@#$#$%^&*',
#         'formData' : {
#             'likes' : {
#                 'L1' : 'Basket Ball',
#                 'L2' : 'Soccer',
#             }, 
#             'watch': {
#                 'anime' : 'Dragon Ball Super',
#             }
#         }
#     }, {
#         'id' : 2,
#         'userId' : 'AdamJensen511997',
#         'name' : 'Adam Jensen',
#         'email' : 'AdamJensen511997@gmail.com',
#         'password' : "It's MD5 Encrypted Password",
#         'formData' : {
#             'likes' : {
#                 'L1' : 'Base Ball',
#                 'L2' : 'Soccer',
#             }, 
#             'watch': {
#                 'anime' : 'Dragon Ball GT',
#             },
#             'kDrama': {
#                 'drama': 'Clean With Passion',
#             }
#         }
#     }   
# ]
    
# for user in userList:
#     data = user.get('formData').get('kDrama')
#     if data:
#         print(data)

# for user in userList:
#     print(user.keys())

# dic_a = {
#     'a': 10,
#     'b': 20,
#     'c': 30,
#     'd': 40,
#     'e': 50,
# } 

# print(dic_a.keys())
# print(dic_a.values())
# print(dic_a)

## Checking ordering of dictionary;
# dic_b = {
#     'abhay': 10,
#     'bobby': 20,
#     'camel': 30,
#     'doggie': 40,
#     'euphoria': 50,
# } 

# print(dic_b.keys())
# print(dic_b.values())
# print(dic_b)

# users = {
#     'user_a' : {
#         'id' : 1,
#         'userId' : 'NeerajSingh511997',
#         'name' : 'Neeraj Singh Junior',
#         'email' : 'NeerajSingh511997@gmail.com',
#         'password' : '3456789kjhg@#$KJHG34567KJHGFDS@#$#$%^&*',
#         'formData' : {
#             'likes' : {
#                 'L1' : 'Basket Ball',
#                 'L2' : 'Soccer',
#             }, 
#             'watch': {
#                 'anime' : 'Dragon Ball Super',
#             }
#         }
#     },
#     'user_b' : {
#         'id' : 2,
#         'userId' : 'AdamJensen511997',
#         'name' : 'Adam Jensen',
#         'email' : 'AdamJensen511997@gmail.com',
#         'password' : "It's MD5 Encrypted Password",
#         'formData' : {
#             'likes' : {
#                 'L1' : 'Base Ball',
#                 'L2' : 'Soccer',
#             }, 
#             'watch': {
#                 'anime' : 'Dragon Ball GT',
#             },
#             'kDrama': {
#                 'drama': 'Clean With Passion',
#             }
#         }
#     }   
# }

## Keys in Complex Dict is getting scattered;
# for keys in users:
#     for key in keys:
#         print(key)

## printing data through list;
# for x in users:
#     for y in sortusers[x]:
#         print(x, " : ", users[x][y])
    
## TypeError: Unhashable List;
# Problem
# dic = {
#     'name': 'Neeraj Singh Junior',
#     ['abc', 'def', 'ghi']: 'Amisha',
# }
# print(dic)

## Solution 
# dic = {
#     'name': 'Neeraj Singh Junior',
#     ('abc', 'def', 'ghi'): 'Amisha'
# }

# print(dic)