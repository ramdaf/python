#grades
num = float(input("Enter the mark:"))
if num < 30:
    print("grade is E. Failed!")
elif num <= 35:
    print("grade is D")
elif num <= 55:
    print("grade is C")
elif num <= 75:
    print("grade is B")
elif num <= 95:
    print("grade is A")
elif num <= 100:
    print("Grade is O")
else:
    print("Invalid Syntax")