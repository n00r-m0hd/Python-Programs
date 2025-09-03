# Write a program to calculate the area of trapezium

#Area of a trapezium A=1\2*(a+b)*height

height=float(input("Enter the height of trapezium\n"))
a=float(input("Enter the value of one side of trapezium\n"))
b=float(input("Enter the value of another side of trapezium\n"))


area=1/2*(a+b)*height

print(f"Area of trapezium is {area}")