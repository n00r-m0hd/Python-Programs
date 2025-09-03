# Write a program to calculate the volume and area of cylinder

# volume = pir**2h surfacearea = 2pir(h+r)

from math import pi 

radius = float(input("Enter the radius of cylinder\n"))
height = float(input("Enter the height of cylinder\n"))

volume = pi*radius**2*height
surfacearea = 2*pi*radius*(height+radius)

print(f"Volume of cylinder {volume}\nSurface area of cylinder {surfacearea}")