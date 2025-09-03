import json

# some JSON:
x =  '{ "name":"Noor Muhammad", "age":24, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])


# import json

# # a Python object (dict):
# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }

# print(type(x))

# # convert into JSON:
# y = json.dumps(x)

# print(type(y))

# # the result is a JSON string:
# print(y)