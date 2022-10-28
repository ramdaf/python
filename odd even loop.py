# odd even loop of 100
#num = int(input("Enter a number"))
print("odd numbers:")
i=0

for i in range(1, 100, 2):
    print(i)

    if i % 3 == 0:
        print("Odd numbers")
    # else:
    #     print("Even numbers")
