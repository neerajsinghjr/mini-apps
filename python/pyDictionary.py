### Eploring Dictionary in Python;

## Below 'dictionry' variable is not the right way of defining python's dictionary;
userList = {
    'user_1' : {
        'id' : 1,
        'first': 'Neeraj',
        'middle': 'Singh',
        'last': 'Junior' ,
        'empId': '20505721',
        'avatar': 'public/image/employee/avatar/img1.jpg',    
    },
    'user_2' : {
        'id' : 2,
        'first': 'Raj',
        'middle': 'Singh',
        'last': 'Bish' ,
        'empId': '20505722',
        'avatar': 'public/image/employee/avatar/img2.jpg',    
    }, 
    'user_3' : {
        'id' : 3,
        'first': 'Yogita',
        'middle': 'Singh',
        'last': 'Deshmukh' ,
        'empId': '20505723',
        'avatar': 'public/image/employee/avatar/img3.jpg',   
    }
}

print(len(userList))

# for x in userList:
#     # print(x.get('user_1').get('empId'))
#     print(x)

## Dic Copy: Copy one item from one dictionary to another dictionary;
# externUserList = userList.copy()
# print(externUserList)
# print(type(userList), ":", type(externUserList))

## Dic Items: items() method returns a list of tuples in (key:value) pair;
# Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}	
# print("Students Name: %s " % Dict.items())

## Checking if the key is present in the Dictionary;
# for key in userList:
#     for in user['key']

## Accessability of Dictionary Items - Beginner Level;
# print(userList['user_1']['first'], userList['user_1']['middle'], userList['user_1']['last'])

## Accessability of Dictionary Items - Intermediate Level;
# for aKey in userList:
#     for bKey in userList[aKey]:
#         print(userList[aKey][bKey])
    
# Sorting an Dictionary;
# akeys = list(userList.keys())
# akeys.sort()
# bkeys = []


# for x in userList:
#     temp = list(userList[x].keys())
#     temp.sort()
#     bkeys += temp
# print(bkeys)
    
    
## User of Instance of in Dict;
# print(isinstance(userList, dict));

### Testing cases for sort;
# Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
# Boys = {'Tim': 18,'Charlie':12,'Robert':25}
# Girls = {'Tiffany':22}
# Students = list(Dict.keys())
# Students.sort()   
# for x in Students:
#     print(x)
# print(Students, type(Students))
# temp = Students.sort()
# print("after sorting", temp)
# for S in Students:
    #   print(":".join((S,str(Dict[S]))))
    
## Converting dictionary to int;
# strDic = str(userList)
# print(type(strDic))

## Adding new member in dictionary;
# sorted(userList)
# print(userList)
# dic_a = {}
# print(type(dic_a))
# dic_a.add('name', 'Neeraj Singh Junior')
# print(dic_a)

## Adding new thing in dictionary;

# temp = {
#     'id' : 3,
#     'first': 'Yogita',
#     'middle': 'Singh',
#     'last': 'Deshmukh' ,
#     'empId': '20505723',
#     'avatar': 'public/image/employee/avatar/img3.jpg',  
# }

# userList['user_1']['new_thing'] = "I'm learning py3"
# print(userList['user_1'])