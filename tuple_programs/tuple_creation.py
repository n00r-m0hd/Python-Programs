tup = (1,2,3,3,4,4)

print(tup)
print(type(tup))

print(tup.count(3))
print(tup.index(4)) 
print(tup[2])   
# print(tup[6])  #IndexError: tuple index out of range


# Below code is not a tuple we can not create tuple like this it will be treated as int type
tuple = (1)

print(type(tuple))

# Rather we create like this if we want insert one element we do like this  


tuple = (1,)

print(type(tuple))
