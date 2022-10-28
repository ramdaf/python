#find the minimum and maximum elemenet in array
array = [23, 445, 44, 65, 901, 35, 82, 10]
minimum = min(array)
print(minimum)
maximum = max(array)
print(maximum)

#arr[] ={1,5,3,2}given random set of numbers,print them in sorted order
ar = {1, 5, 3, 2}

arry = list(ar)
array = sorted(arry)
print(array)

#find a program to reverse an array
array = ['Qatar', 'China', 'Rome', 'Korea', 'India']
array.reverse()
print(array)

#create 3 arrays and find the common element in these array
array = [23, 445, 44, 65, 6666, 901, 35, 82, 10]
arr1 = [23, 45, 235, 345.2, 432, 11, 6666]
arr2 = [34, 545, 23, 67, 34, 6666, 1.3234]
for i in array:
    if i in arr1 and arr2:
        print(i)
#using set intersection
array = [23, 445, 44, 65, 6666, 901, 35, 82, 10]
arr1 = [23, 45, 235, 345.2, 432, 11, 6666]
arr2 = [34, 545, 23, 67, 34, 6666, 1.3234]
setarray = set(array)
setarr1 = set(arr1)
setarr2 = set(arr2)
p = setarray.intersection(setarr1, setarr2)
print(p)

#find the factorial of a number using array
array = [23, 445, 44, 65, 901, 35, 82, 10]



