# Write a program to calculate the volume and Surface area of a pyramid

# Polygon base + triangular sides
# 	V = (1/3) × base area × height	
# Depends on base (square: SA = base area + 4 × triangle area)]

baseArea = float(input("Enter the base area of polygon\n"))

height = float(input("Enter the height of polygon\n"))

volume = 1/3*(baseArea*height)

print(f"Volume of polygon is {volume}")

triangleArea = float(input("Enter the triangle area of polygon\n"))

surfaceArea = baseArea+4*triangleArea

print(f"Surface area of polygon is {surfaceArea}")