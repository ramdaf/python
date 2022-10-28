q = lambda a:a*20
print(q(2))

n1 = lambda a,s:a+s
print(n1(3,4))

#lambda function
def function(n):
    return lambda  a:a*n
result = function(5)
print(result(11))

def function():
    return lambda a:a*a
r = function()
print(r(20))

