# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,between 2000 and 3200
# (both included).The numbers obtained should be printed in a comma-separated sequence on a single line.

start = 2000
stop = 3200
def number():
    for i in range(start, stop+1):
        if i%7 == 0 and i%5 != 0:
            print(i, end=",")
number()

#With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such
#that is an integral number between 1 and n (both included). and then the program should print the
 #dictionary.
#Suppose the following input is supplied to the program:8



