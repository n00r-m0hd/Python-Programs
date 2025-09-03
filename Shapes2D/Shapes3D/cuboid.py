# Write a program to calculate volume and area of cuboid

# Volume of cuboid is V=l*w*h area is SA = 2 × (lw + lh + wh) or SA=2(lb+lh+bh)

length=int(input("Enter the length of Cuboid\n"))
width=int(input("Enter the width/breadth of Cuboid\n"))
height=int(input("Enter the height of Cuboid\n"))

volume=length*width*height

print(f"Volume of Cuboid is {volume}")

area=2*((length*width) + (length*height) + (width*height))

print(f"Area of Cuboid is {area}")