# Write a program to calculate the volume and Surface Area of a hemisphere

# V = (2/3) × π × r³ SA = 3 × π × r²

from math import pi

radius = float(input("Enter the radius of a hemisphere\n"))

volume = 2/3*(pi*radius**3)

surfaceArea = 3*pi*radius**2

print(f"Volume of a hemisphere is {volume}\nSurface Area of hemisphere is {surfaceArea}")
