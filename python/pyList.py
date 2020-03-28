### Exploring List in Python;

## Declaraing list;
singleList = [ 1, 'neeraj', 'running', 20000, 'explorer']
complexList = [
    [
        1, 'neeraj', 'running', 20000, 'explorer', 'asus zenfone', 'vlc media player'
    ], [
        2, 'manav', 'blogs', 30000, 'gallery'
    ], [
        3, 'yogita', 30000, 'gallery'
    ]
]
singleList[0] = 1001
singleList[1] = "Hello World"

## Appending element at list;
# complexList[0].append('Hello Lucky')
# complexList[1].append('Hello Jin')
# complexList[2].append('Hello Sara')

## Inserting new element in a list;
# complexList.insert(0, "Housefull")
# complexList.insert(1, ['ello', 'ell', 'ellooo', 'elloo'])

## Poping element from list;
# print(complexList.index("neeraj"))

## Printing Elements;
# print(complexList)

## Indexing of elements in List;
# for x in complexList:
#     print(x.index())
#     for y in x:
#         print(y.index())

complexList.append("Umbrella")
complexList.append("Laptop")

## Iterating values in complex list;
# for x in  complexList:
#     for y in x:
#         print("Type: ", type(y), '|', y)
# print(complexList)

## Pop elements from the list;
# popped = complexList.pop()
# print(popped)

## Observing samples;
# list = ['larry', 'curly', 'moe']
# list.append('shemp')        
# list.insert(0, 'xxx')       
# list.extend(['yyy', 'zzz'])  
# print(list)
# print("Index : ", list.index('curly') + 1) 
# list.remove('curly')
# print("Before Removed: ", list)
# popped = list.pop(1)
# print("After Removed: ", list)

## Reverse index in python;
list = [1, 2, 3, 4, 5, 6]
print(list[:-1])    # print length-1 of list;
print(list[::-1])   # print list in reverse order;
print(list[-1::])   # print the -1 index element;

## list() method;

temp = ("ghj", "fgh", "xcv")
print(type(temp))
tmp = list(temp)
print(type(tmp))