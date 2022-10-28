#multiplication table
num = int(input("Enter a number:"))
b = int(input("Enter the range:"))
i = 1
for j in range(b):
    i = j * num
    print(j, "*", num, "=", i)
