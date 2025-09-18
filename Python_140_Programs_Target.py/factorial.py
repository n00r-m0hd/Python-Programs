num = int(input("Enter an Integer\n"))

factorial = 1

if num < 0:
    print("Factorial does not exist for negative numbers\n")

elif num == 0:
    print("Factorial of zero is always one")

elif num > 0:
    for i in range(1, num+1):
        factorial = factorial * i
    print(f"Factorial of {num} is {factorial}")
