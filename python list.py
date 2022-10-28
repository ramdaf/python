# python list
fruits = ['apple', 'orange', 'pineapple', 'plum', 'kiwi', 1, 2, 3, True, False, True]
print(fruits[-1])
print(fruits[3])
print(len(fruits))

#list properties
#list construct using list constructor
a = list((1, 'orange'))
print(a)
#accesing list items
my_list = ['apple', 'orange', 'pineapple', 'plum', 'kiwi', 1, 2, 3, True, False, True, 5]
print(my_list[0])
print(my_list[-2])
#list slice
print(my_list[2:5])
print(my_list[2:])
print(my_list[:5])#value accessing
print(my_list[-10:-1])#-ve indexing
print(my_list[-10:])
print(my_list[:-9])
#membership operator
if 'grapes' in my_list:
    print("apple found")
else:
    print("item not found")
#changing the item value(updation)

my_list[0] = 'cherry'
print(my_list)
my_list[2:3] = ['a', 'b']
print(my_list)
my_list[3:4] = ['b1', 'b2', 'b3']
print(my_list)
#insert()
my_list.insert(4, 'qwe')
print(my_list)
#append()
my_list.append("sample")
print(my_list)
#extend() append/merge elements from another list
my_list.extend(fruits)
print(my_list)
#remove list items
#remove()
my_list.remove('b1')
print(my_list)
#pop() indexing usage
my_list.pop(5)
print(my_list)
my_list.pop()
print(my_list)
#del
# del my_list[0]
# print(my_list)

