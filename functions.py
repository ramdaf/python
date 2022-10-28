#function

def name(a,b,c):
    print("The younger child name is:", c)
name(a = "ram",b = "sam",c = 'rumi')

#arbitarary keyword
def child(**args):
    print("name is:", args['lname'])
child(name = 'tom', lname ='cruise', age=25, city = 'colombo')

#default parameter
def my_funct(country="Norway"):
    print("My country is:"+country)
my_funct()

#passing list as arguements
def foodlist(a):
    for x in a:
        print(x)
list = [1,2,3,'a','b','c']
foodlist(list)

#assign a different name to function and call the function using new name

def function():
    print("hello")
name = function
name()

#generate a python list of all the even numbers b/w 9 to 40 using function
def even(a):
    for i in range(9,40):
        if i%2==0:
            print(i)
number = []
even(number)


#write a program to find lcm of a number using function

