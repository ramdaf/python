student = {'name':"aju", "roll_no" : 15, "mark":'500', "place":'kochi', 'subject':'IT'}
print(student)
print(type(student))
print(len(student))

#accessing dict items using key
student = {'name':"aju", "roll_no" : 15, "mark":'500', "place":'kochi', 'subject':'IT'}
print(student["mark"])

#accessing using get method
student = {'name':"aju", "roll_no" : 15, "mark":'500', "place":'kochi', 'subject':'IT'}
print(student.get('place'))

#accessing keys
student = {'name':"aju", "roll_no" : 15, "mark":500, "place":'kochi', 'subject':'IT'}
print(student.keys())
print(student.values())
print(student.items())

#add a record
student = {'name':"aju", "roll_no" : 15, "mark":500, "place":'kochi', 'subject':'IT'}
student['age'] = '25'
print(student)

#change values
student = {'name':"aju", "roll_no" : 15, "mark":500, "place":'kochi', 'subject':'IT'}
student["place"] = "calicut"
print(student)

#update()
student = {'name':"aju", "roll_no" : 15, "mark":500, "place":'kochi', 'subject':'IT'}
student.update({"mark":450})
print(student)

#pop method to remove
student = {'name':"aju", "roll_no" : 15, "mark":500, "place":'kochi', 'subject':'IT'}
student.pop("roll_no")
print(student)
student.popitem() #last item removed
print(student)

#using delete method
student = {'name':"aju", "roll_no" : 15, "mark":'500', "place":'kochi', 'subject':'IT'}
del student["roll_no"]
print(student)

#for lopp in dict
student = {'name':"aju", "roll_no" : 15, "mark":'500', "place":'kochi', 'subject':'IT'}
for i in student:
    print(student[i])

#using function
student = {'name':"aju", "roll_no" : 15, "mark":'500', "place":'kochi', 'subject':'IT'}
for i in student.keys():
    print(i)

#using function
student = {'name':"aju", "roll_no" : 15, "mark":'500', "place":'kochi', 'subject':'IT'}
for i, j in student.items():
    print(i, j)

#copy method
student = {'name':"aju", "roll_no" : 15, "mark":'500', "place":'kochi', 'subject':'IT'}
new = student.copy()
print(new)

#dict method
new = {'name':"aju", "roll_no" : 15, "mark":'500', "place":'kochi', 'subject':'IT'}
d = dict()
print(d)

#nested dictionARIES
student = {'name':"aju", "roll_no" : 15, "mark":'500', "place":'kochi', 'subject':'IT'},  {'name':"aju", "roll_no" : 15, "mark":'500', "place":'kochi', 'subject':'IT'},  {'name':"aju", "roll_no" : 15, "mark":'500', "place":'kochi', 'subject':'IT'}
print(student)

#convert 2 lists into dictionary
list = [1, 2]
list1 = ["apple",'banana']
new ={}
for i in range(len(list)):
    new.update({list[i]:list1[i]})
print(new)

#convert 2 dictionary to a dictionary
d1 ={1: 'apple', 2: 'banana'}
new = {'name':"aju", "roll_no" : 15, "mark":'500', "place":'kochi', 'subject':'IT'}
d1.update(new)
print(d1)

#print values
dict = {'class':{"student":{'name':"mike", "marks":{"physics":100,"history":92,"maths":90}}}}
gd = dict["class"]["student"]["marks"]["history"]
print(gd)
