a = 1
b = 34
c = 10
sum = a+b+c
print("sum=", sum)

#function
sum=0
n1 = int(input("Enter a number:"))
n2 = int(input("Enter next number:"))
n3 = int(input("Enter next number:"))
def addition(a, b, c):
    sum = a + b + c
    print("sum is", sum)


addition(n1,n2,n3)

#another method
sum=0
def addition(a, b, c):
    sum = a + b + c
    print("sum is", sum)
n1 = int(input("Enter a number:"))
n2 = int(input("Enter next number:"))
n3 = int(input("Enter next number:"))
addition(n1,n2,n3)


#factorial of a number using recursion
def factorial(n1):
    fact = 1
    for i in range(1, n1+1):
        fact = fact*i
    print("factorial of a number", fact)

num = int(input("Enter a number:"))
factorial(num)

#to make a calculator add,sub,multiply and divide,modulus
def add(a,b):
    sum = 0
    sum = a+b
    print("sum is",sum)
def sub(a,b):
    sum1 = 0
    sum1 =a-b
    print("sum is:",sum1)
def multiply(a,b):
    sum2 = 0
    sum2 =a*b
    print("sum is:",sum2)
def divide(a,b):
    sum3 = 0
    sum3 = a/b
    print("sum is:",sum3)
def modulus(a,b):
    sum4 = 0
    sum4 = a%b
    print("sum is:",sum4)

n1 = int(input("Enter a number:"))
n2 = int(input("Enter another number"))
print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.modulus")
choice = int(input("Enter your choice:"))
if choice == 1:
    add(n1, n2)
elif choice == 2:
    sub(n1, n2)
elif choice == 3:
    multiply(n1, n2)
elif choice == 4:
    divide(n1, n2)
elif choice == 5:
    modulus(n1, n2)
else:
    print("Invalid choice")




#


