#find type & length of tuple
fruits = ("apple", 'cherry', 'berry', 'orange')
print(fruits)
print(type(fruits))
print(len(fruits))

#accessing second largest item
number = (23,45,12,454,324,5641,4554,00)
#number.sort()
print(number[-4])

#convert tuple into list and change items
fruits = ("apple", 'cherry', 'berry', 'orange')
h = list(fruits)
h[2] = "guava"
print(h)

#convert tuple to list & append new element

h.append("hello")
print(h)

#append new list
fruits = ("apple", 'cherry', 'berry', 'orange')
number = (23,45,12,454,324,5641,4554,00)
fruits += number
print(fruits)

#remove tuple
fruits = ("apple", 'cherry', 'berry', 'orange')
g = list(fruits)
g.remove("apple")
print(g)

#use for loop
fruits = ("apple", 'cherry', 'berry', 'orange')
for i in fruits:
    print(i)

#print tuple in multiply times
number = (23,45,12,454,324,5641,4554,00)
f = number*5
print(f)

#join tuples
number = (23,45,12,454,324,5641,4554,00)
fruits = ("apple", 'cherry', 'berry', 'orange')
sum = number + fruits
print(sum)

#tuple methods
#1. count functions
number = (23,00,45,12,454,00,324,12,5641,4554,00,12)
print(number.count(12))

#use while loop
number = (23,00,45,12,454,00,324,112)
i = number[0]
while i < len(int(number)):
    print(i)
    i = i+1


