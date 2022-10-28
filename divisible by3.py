num = int(input("Enter a number:"))
a = num % 10
if a == 0:
    print("it  is not divisible")
elif a % 3 == 0:
    print("it is divisible by 3")
else:
    print("it is not divisible by 3")
