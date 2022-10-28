
#tried attempt
def function(n):
    return abs(n - 0)
list = [23,34,0,-23,-65]
list.sort(key = function)
print(list)

#real one
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]

thislist.sort(key = myfunc)

print(thislist)