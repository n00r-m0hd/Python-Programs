num = int(input("Enter an Integer\n"))

if num == 0:
    print(f"{num} is a zero number please enter a valid number")
elif num%2 != 0:
    print(f"{num} is an Odd number")

else:
    print(f"{num} is an Even number")