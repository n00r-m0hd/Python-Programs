# Write a program to calculate the volume and the Surface area of a cone

# V = (1/3) × π × r² × h   SA = πr(l + r) (l = slant height)

from math import pi

radius=float(input("Enter the radius of cone\n"))

height=float(input("Enter the height of cone\n"))

volume = 1/3*(pi*radius**2*height)

print(f"Volume of cone is {volume}")

sheight=float(input("Enter the slang height of cone\n"))

surfaceArea = pi*radius*(sheight+radius)

print(f"Surface Area of cone is {surfaceArea}")