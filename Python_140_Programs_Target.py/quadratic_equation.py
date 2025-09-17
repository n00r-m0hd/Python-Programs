import math

#Input coefficients

a = float(input("Enter the value of coefficient a\n"))
b = float(input("Enter the value of coefficient b\n"))
c = float(input("Enter the value of coefficient c\n"))

#Calculate the discriminant

discriminant = b**2 - 4*a*c

# Check if discriminant is positive, negative, or zero

if discriminant>0:
    #Two real and distict roots 

    root1 = (-b + math.sqrt(discriminant)/(2*a))

    root2 = (-b - math.sqrt(discriminant)/(2*a))

    print(f"Root 1 : {root1}")
    print(f"Root 2 : {root2}")


elif discriminant == 0:
    #One real root (repeated)

    root = -b/(2*a)
    print(f"Root : {root}")

else:
    #complex roots

    real_part = -b /(2*a)
    imagenary_part = math.sqrt(abs(discriminant)/(2*a))
    print(f"Root 1: {real_part} + {imagenary_part}i")
    print(f"Root 2: {real_part} -{imagenary_part}i")