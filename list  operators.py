fruits = ['apple', 'orange', 'pineapple', 'plum', 'kiwi', 1, 2, 3, True, False, True]
print(fruits)
# for i in fruits:
#     print(i)
i = 0
while i < len(fruits):
    print(fruits[i])
    i = i + 1

new = []   #new list
if 'apple' in fruits:
    new.append('apple')
    print(new)

# members which  have d
flowers = ['daisy', 'jasmine', 'rose', 'daffodil', 'fadi', 'chrysanthmum', 'lavander']
nl = []
for i in flowers:
    if "d" in i:
        nl.append(i)

print(nl)

# members which start from d


#sort() operations
flowers.sort()
print(flowers)
# fruits.sort()
# print(fruits)

#sort in descending order
flowers.sort(reverse=True)
print(flowers)
numbers = [1, 4, 5, 2, 34, 76, 24, 54, 1006, 500]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

#reverse a list
numbers.reverse()
print(numbers)

#copy a list
newlist = fruits.copy()
print(newlist)

#to join 2 lists
list1 = [1, 5, 2, 85, 234]
list2 = ["sa", 'sde', 'rtew', 'edgfg']
llist = list2+list1
print(llist)
