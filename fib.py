#fibonacci series upto 10 terms
num = 10
n1 = 0
n2 = 1
print("Fibonacci series:")
print(n1)
print(n2)
for i in range(0, num):
    n3 = n1+n2
    n1 = n2
    n2 = n3
    print(n3)
