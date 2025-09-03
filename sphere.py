"""

Term	Description
Center	The fixed point in the middle of the sphere
Radius (r)	The distance from the center to any point on the surface
Diameter (d)	The distance across the sphere, passing through the center (d = 2r)
Surface Area	The total area that covers the outside of the sphere
Volume	The amount of space inside the sphere
Key Formulas

Here are two essential formulas for spheres:

1. Surface Area (SA):SA=4PIr2

This tells you how much surface is on the outside of the sphere.

2. Volume (V): V= 4/3PIr3

This tells you how much space is inside the sphere.

"""
from math import pi

r=6

v=4/3*pi*r**3

print(f"Volume of sphere is {v}")