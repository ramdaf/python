import json
x = '{"name":"ram","age":30,"city":"kochi"}' #json
# print(x["name"])
y = json.loads(x)  #parsing
print(y["name"])
print(type(x))

#converting python dict into json

f = {"name": "ram", "age": 30, "city": "Kochi"}
j = json.dumps(f)  # dumps
print(j)
print(type(j))
print(json.dumps(["apple", "kiwi", "orange"]))
print(json.dumps(['apple',  67, 'kiwi', 'orange', 45, 56]))
print(json.dumps([23, 45,45]))