
fruits = ["Banana","Apple","Orange","Mango","Pomegranate"]

numbers = [1,2,3,4,5,6,7,8,9,10]

numbers.append(11) # Add item add the end of the list

numbers.insert(0,1) #Inserts at specific index

my_num = [12,13,14,15] 

numbers.extend(my_num) #Add multiple items

numbers.remove(1) #Remove first occurrence of x

numbers.pop() # Remove an item from the end

print(numbers.pop(3)) #Remove and return item at index

# numbers.clear()  # Removes all elements from a list

x = numbers.index(13) # Find the index of first occurrence of x

print(x)

y = numbers.count(10)

print(y)

numbers.reverse() #It does not take any arguments. It returns None. reverse the list

print(numbers)

numbers.sort()  # Sort list (ascending by default)

print(numbers)

new_list = sorted(numbers) #Returns new sorted list

print(new_list)