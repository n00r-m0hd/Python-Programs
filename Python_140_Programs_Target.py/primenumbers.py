# Write a python program to check whether a given number is prime number or not

num = int(input("Enter an Integer\n"))

flag = False

if num == 1:
    print(f"{num} is not a prime number")

elif num >1:
    for i in range(2, num):  # Check for factors
        if num%i == 0:
            flag = True  #If factor is found set flag to True

            break  # Break out of loop

# Check if flag is True
if flag:
    print(f"{num} is a not prime number")

else:
    print(f"{num} is a prime number") 