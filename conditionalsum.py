# Conditional Sum to 20

# Write a Python program to sum two given integers. 
# However, if the sum is between 15 and 20 it will return 20.

int1 = int(input("Enter the value of first Integer\n"))
int2 = int(input("Enter the value of second Integer\n"))


sum = int1+int2

print(f"Sum of {int1} and {int2} is {sum}")

for i in range(15,21):
    if sum==i:
        sum=20
        print(f"Now sum is {sum}")
        break