#print set, find type and length of the set
amb = {"cherry", 'apple', "plum", "berry"}
print(amb)
print(len(amb))
print(type(amb))

#tuple to set
SA=('farsa', 'allu', 'ola')
print(SA)

#Accessing set items
amb = {"cherry", 'apple', "plum", "berry"}
for i in amb:
    print(i)

#print new value,remove and discard item,discard function didn't show any error
amb = {"cherry", 'apple', "plum", "berry"}
amb.add("kiwi")
print(amb)
amb.remove("berry")
print(amb)
amb.discard("plum")
print(amb)
# amb.discard("mango")
# print(amb)
# amb.remove("mango")
# print(amb)

#add a set to another set
am = {'plum', 'apple', 'kiwi', 'cherry', 'berry'}
an = {34, 45, 345, 132, 454}
am.update(an)
print(am)

#join sets and union,intersection
a = {'plum', 'apple', 'kiwi', 'cherry', 'berry'}
b = ['56', '67', '65']
g = a.union(b)
print(g)

#intersection
g = {'plum', 'apple', 'kiwi', 'cherry', 'berry'}
h = {4, 6, 79, 46, "kiwi"}
f = g.intersection(h)
print(f)

#symmetric difference ,symmetric difference_update
g = {'plum', 'apple', 'kiwi', 'cherry', 'berry'}
h = {4, 6, 79, 46, "kiwi"}
f = g.symmetric_difference(h)
print(f)