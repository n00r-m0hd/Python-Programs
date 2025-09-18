# Write a python program to calculate the sum N numbers

num = int(input("Enter an Inetger"))

sum = 0

for i in range(num+1):
    sum = sum + i 

print(f"Sum of {num} numbers is {sum}")