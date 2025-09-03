# Write a program to calculate the voulme and area of a sphere

#volume=4/3(pi*r**3) area surface area = 4*pi*r**2

from math import pi

radius=float(input("Enter the value of radius\n"))

volume = 4/3*(pi*radius**3)

area = 4 * pi * radius**2


print(f"Volume of sphere is {volume}\n Area of Sphere is {area}")