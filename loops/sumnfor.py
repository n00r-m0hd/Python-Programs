# Write a program to calculate the sum of n numbers

num = int(input("Enter an Integer\n"))

sum = 0

for i in range(1,num+1):
    sum = sum + i

print(f"Sum of {num} numbers is {sum}")